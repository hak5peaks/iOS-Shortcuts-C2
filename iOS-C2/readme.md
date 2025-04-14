# SSH Server Set Up

We are using a custom made SSH server to receive data from the iOS device using SSH. Using python and paramiko we have created a SSH server that does not serve a shell but however logs sent data from its users allowing us to use the SSH protocol to exfil data from the iOS Device

Setup is easy simply install the required packages 
```
> pip install -r requirements.txt
> or
> pip install paramiko==2.12.0
>
> python3 C2.py
```
The SSH server will generate a host key if there is not one already. it will use this key each time you start the server 

To enable custom responses for C2 payloads you will need to have the Custom_Commands.txt file, this file defines what commands the SSH server should be listening for and how to respond to them. We can use this within shortcuts by do "If shell Has Response" Or "If Shell Has No Response" as a link to the next action, we can also use the output of the commands as variables inside of the C2 Payloads. By default if the server receives a command that is no inside of the table it will not response

Example video: https://github.com/Peaakss/iOS-Shortcuts-C2/assets/115900893/460c83e8-48f4-43da-956c-58d6570c2c60 (need to change 2 a gif)

# Custom Commands

the `custom_commands.txt` file is used to determine if or if not the SSH server responds to a certain command. 

```
send_response:1
send_no_response:
command1:1
command2:
```
**picture of shortcut SSH node**
This file uses a matching system. If it receives `command1` from the client, the C2 server will check this file to determine if it should responde and what it should respond with. 

# Users 

the `users.txt` file is used for SSH authentication, this is a simple txt file containing a table of allowed auth users and their passwords, this can be used for device management. 
```
user:password
```
**picture of shortcut SSH node**
