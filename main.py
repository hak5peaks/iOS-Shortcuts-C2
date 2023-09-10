import paramiko
import socket
import threading
import datetime

class CommandHandler(paramiko.ServerInterface):
    def __init__(self, users):
        self.event = threading.Event()
        self.users = users
        self.username = None

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_exec_request(self, channel, command):
        decoded_command = command.decode('utf-8')
        if self.username:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
            print("----------------------------------------") 
            print(f"Connection From SSH User: {self.username} | Time: {timestamp} | {decoded_command}")
            print("----------------------------------------") 
            with open("commands.txt", "a") as file:
                file.write(f"Timestamp: {timestamp}, User: {self.username}, Command: {decoded_command}\n")
        return True


    def check_auth_password(self, username, password):
        if username in self.users and self.users[username] == password:
            self.username = username  # Store the current username
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
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(":")
                config[key.strip()] = value.strip()
    return config

def main():
    config = read_config("config.txt")
    host = config.get("host", "0.0.0.0")
    port = int(config.get("port", 22))

    host_key = load_host_key()
    if host_key is None:
        print("Generating new RSA host key...")
        host_key = paramiko.RSAKey.generate(2048)
        host_key.write_private_key_file('host_key.pem')

    users = read_users("users.txt")

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
    print("                  iOS C2 Beta 2 (Need Cool Name)")
    print("                 ---------------") 
    print(" ")
    print(f"[*] Listening on {host}:{port}")
    print("----------------------------------------") 

    while True:
        client, addr = server_sock.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        transport = paramiko.Transport(client)
        transport.add_server_key(host_key)
        handler = CommandHandler(users)

        try:
            transport.start_server(server=handler)
        except paramiko.SSHException as e:
            print(f"[-] SSH negotiation failed: {str(e)}")
            client.close()
            continue

            while transport.is_active():
                if handler.event.is_set():
                    break

            transport.close()
        except ConnectionResetError:
            print("----------------------------------------")

if __name__ == "__main__":
    main()
