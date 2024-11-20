—------------------------------
# iOS C2 Documentation

`KNOWN ISSUE: Windows Unicode | if you are hosting on windows replace line 40 "with open("commands.txt", "a") as file:" with "with open("data/commands.txt", "a", encoding="utf-8") as file:"`
—------------------------------

Welcome, this project is dedicated to researching the iOS shortcuts application to discover vulberabilies for use to C2 most iOS devices using a mix of tools such as a custom SSH server, .shortcut files and keystroke injection to deliver a malicous shortcut file written to C2 iOS devices


# SSH Server Set Up

We are using a custom made SSH server to receive data from the iOS device using SSH. Using python and paramiko we have created a SSH server that does not serve a shell but however logs sent data from its users allowing us to use the SSH protocol to exfil data from the iOS Device

Setup is easy simply install the required packages 
```
> pip install requirements.txt
> or
> pip install paramiko==2.12.0
```
The SSH server will generate a host key if there is not one already.  it will use this key each time you start the server 

To enable custom responses for C2 payloads you will need to have the Custom_Commands.txt file, this file defines what commands the SSH server should be listening for and how to respond to them. We can use this within shortcuts by do "If shell Has Response" Or "If Shell Has No Response" as a link to the next action, we can also use the output of the commands as variables inside of the C2 Payloads. By default if the server receives a command that is no inside of the table it will not response

Example video: https://github.com/Peaakss/iOS-Shortcuts-C2/assets/115900893/460c83e8-48f4-43da-956c-58d6570c2c60


<p align="center">
  <img src="https://github.com/Peaakss/iOS-Shortcuts-C2/assets/115900893/3d98cf67-2919-407a-9a4b-d2e2583d9425" alt="Image Description" width="500" height="auto">
</p>




# HTTP Server Setup 

The Http server is very simple. This server logs all directory requests. we can use this as a data exfil option. using the http server helps as it does not need as much configuration from the device, however it is not able to do C2 Functions like the SSH Server. HTTP exfil is also not covert, meaning it has to open a new appliction everytime it is called unlike the SSH server

<p align="center">
<img src="https://github.com/Peaakss/iOS-Shortcuts-C2/assets/115900893/14263c16-d88e-48b7-ac71-3b729b50aacc" alt="Image Description" width="500" height="auto">
</p>

# Apple has declared this research a non-security issue as of 2/24/24, 3:50 PM

<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/483212b1-8b66-4eb8-8880-89fdeb823347" alt="Image Description" width="500" height="auto">
</p>

# iOS Shortcut Payload 

We are using a premade .shortcut file from another iOS device for the shortcut we will be using to gather information. These files are signed and has a Root CA certification that allow them to be download and ran with the shortcuts application 
<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/d93f1553-7553-411d-a876-a404d95fc1ed" alt="Image Description" width="500" height="auto">
</p>
This file should be downloaded onto the device and once opened should directly be imported to the Shortcuts application. 

# iOS Settings 

Once the file is imported and on the device we need to configure the iOS device to allow it to run the shortcut. Navigating to Settings -> Shortcuts -> Advanced we can find the setting to Allow Running Scripts, enabling this will allow us to run SSH scripts and run Javascript on websites from the Shortcuts App. Enabling Allow Sharing Large Amounts Of Data will also allow for large amounts of data to be sent over SSH 
<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/62c9a031-f8be-4dd0-ad6b-a86dd8159a56" alt="Image Description" width="500" height="auto">
</p>

#Connecting Shortcuts to Automations 

To enable the shortcut to act as a logic bomb or even run it as a loop we will need to connect the shortcut to a automation 

There are several different trigger options for Automations

<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/23e5ee5b-5413-4d6c-b217-2167746b69b9" alt="Image Description" width="500" height="auto">
</p>
<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/d0cc33e0-fc41-49a5-889e-bb97317fa0fe" alt="Image Description" width="500" height="auto">
</p>
<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/8ea993a6-65c4-442f-a967-a3b60569d8fe" alt="Image Description" width="500" height="auto">
</p>
Once a trigger is selected and configured and we are inside the action menu we will want to add a “Run Shortcut” action so once the automation is ran it will run our shortcut 
<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/a8defb14-1990-4082-95dc-722b8805a20f" alt="Image Description" width="500" height="auto">
</p>
Once we complete setting up the shortcut we will want to disable ask before running and notify when ran this will help in keeping the shortcut hidden on the device, keep in mind some automation triggers do not allow you to turn these settings off such as Message and email 
<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/9df12376-29d7-45f2-bf9a-b3e2074a8045" alt="Image Description" width="500" height="auto">
</p>
# More context 

Ideally to deliver and run our shortcut we will want to have a custom web server hosting our .shortcut file. It is possible to do use all by hand with physical unlocked access to the device, however we can use keystroke injection to automate and speed up the process using a device like the O.MG cable 



