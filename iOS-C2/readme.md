# SSH Server Set Up

The Shortcuts C2 listener utilizers the Paramiko library to emulate a legitimate SSH server. This SSH server will emulate legitimate user authentication and receive client commands without having a direct connection to a system shell. This setup allows us to listen to client inputs and send back predetermined responses to the client. 

These reponses can be utlizied within the Shortcuts application in diffrent ways such as `If SSH has value`/`If SSH has no value` you can also store the response from the C2 as a string to use within the shortcut. 

Setup is easy, simply install the required packages 
```
> pip install -r requirements.txt
> or
> pip install paramiko==2.12.0
>
> python3 C2.py
```
The SSH server will generate a host key if there is not one already. it will use this key each time you start the server. By default the SSH server will listen on all intefaces on port 22. This can be easily changed inside of the `config.txt` file
```
host:0.0.0.0
port:22
```
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
<p align="center">
  <img src="https://github.com/user-attachments/assets/71ed141e-f748-47a4-b09d-914437b4d897" alt="Image Description" width="300" height="auto">
</p>

