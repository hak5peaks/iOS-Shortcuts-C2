import paramiko
import socket
import threading
import datetime
import os

#If there is a command sent that is not inside of the custom_commands.txt file then the default response is nothing - will add this to README soon

class CommandHandler(paramiko.ServerInterface):
    def __init__(self, users, custom_commands_file):
        self.event = threading.Event()
        self.users = users
        self.username = None
        self.custom_commands = self.load_custom_commands(custom_commands_file)


    def load_custom_commands(self, filename):
        custom_commands = {}
        try:
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        command, response = line.split(":")
                        custom_commands[command] = response
        except FileNotFoundError:
            pass  
        return custom_commands



    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_exec_request(self, channel, command):
        decoded_command = command.decode('utf-8')
        if self.username:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("----------------------------------------") 
            print(f"Received command from {self.username} at {timestamp}: {decoded_command}")
            print("----------------------------------------") 
            with open("logs.txt", "a") as file:
                file.write(f"Timestamp: {timestamp}, User: {self.username}, Command: {decoded_command}\n")
                file.write(f"----------------------------------------------------------------------------")

            if decoded_command.strip() in self.custom_commands:
                response = self.custom_commands[decoded_command.strip()]
                channel.send(response.encode("utf-8"))
                channel.close()
                return True
            else:
            	channel.close()
            	return True
                


        return False
            

    def check_auth_password(self, username, password):
        if username in self.users and self.users[username] == password:
            self.username = username
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

def load_host_key():
    try:
        return paramiko.RSAKey(filename='host_key.pem')
    except paramiko.PasswordRequiredException:
        raise
    except:
        return None

def read_users(filename):
    users = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                username, password = line.split(":")
                users[username] = password
    return users

def read_config(filename):
    config = {}
    if not os.path.exists(filename):
        print(f"Creating {filename} with default values.")
        with open(filename, "w") as file:
            file.write("host: 0.0.0.0\n")
            file.write("port: 22\n")

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(":")
                config[key.strip()] = value.strip()
    return config

def create_default_users_file(filename):
    if not os.path.exists(filename):
        print(f"Creating {filename} with default users.")
        with open(filename, "w") as file:
            file.write("user:password\n")

def main():
    config = read_config("config.txt")
    host = config.get("host", "0.0.0.0")
    port = int(config.get("port", 22))
    custom_commands_file = "custom_commands.txt"
    users_file = "users.txt"

    host_key = load_host_key()
    if host_key is None:
        print("Generating new RSA host key...")
        host_key = paramiko.RSAKey.generate(2048)
        host_key.write_private_key_file('host_key.pem')

    create_default_users_file(users_file)
    users = read_users(users_file)

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(5)

    print(""" 
               ▌▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▌            
                ▄ ███ ▀████████▌ ███ ▄             
             ▄██▀ ███▌          ▐███ ▀██▄          
           ▄██▀ ▄███▀ ▄████████▄ ▀███▄ ▀██▄       
         ▄███▀ ████ ▄████████████▄ ████ ▐███▄      
        ████▀ ████▌ ▀▀           ▀▀ ▐████ ▀████    
       ████   ██████▄▄██████████▄▄██████   ████   
      ████  █▌ ▀█████████▀▀▀▀█████████▀ ▄█  ████   
     ████  ▄███  ▐████▀        ▀████▌  ███▌  ███▌  
     ███▌  ███▌  ████            ████  ████  ████  
     ███▌  ███▌  ███▌            ▐███  ▐███  ████  
     ███▌  ███▌  ████            ████  ████  ████  
     ████  ▀███   ████▄        ▄███████▄▀█▌  ███▌  
      ████  ████▄  ▀█████▄▄▄▄█████▀ ████ ▀  ████   
       ████  ▀████▄  ▀▀████████▀▀  ▄████   ████   
        ████▄  ▀████▄▄          ▄▄████▀  ▄████    
         ▀████▄  ▀██████████████████▀  ▄████▀      
           ▀████▄    ▀▀▀██████▀▀▀   ▄▄████▀       
             ▀▀  ▄▀           ▄▄▄███████▀          
              ▄███▄█████████████████▀             
             █████████▀▀▀▀▀▀▀▀▀▀                  
            ████████▄                              
           ██▀                                    
                           
             """)
    print("                  iOS C2 Beta 2")
    print("                 ---------------") 
    print("                 Commands Update")
    print(" ")
    print(f"[*] Listening on {host}:{port}")
    print("----------------------------------------") 

    while True:
        try:
            client, addr = server_sock.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

            transport = paramiko.Transport(client)
            transport.add_server_key(host_key)
            handler = CommandHandler(users, custom_commands_file)

            try:
                transport.start_server(server=handler)
            except paramiko.SSHException as e:
                print("----------------------------------------")
                print(f"[-] SSH negotiation failed: {str(e)} | POSSIBLE NETWORK SCAN!")
                print("----------------------------------------")
                client.close()
                continue

            while transport.is_active():
                if handler.event.is_set():
                    break

            transport.close()
        except ConnectionResetError:
            print("----------------------------------------")
            print("ConnectionResetError: Connection reset by peer")
            print("----------------------------------------")

if __name__ == "__main__":
    main()
