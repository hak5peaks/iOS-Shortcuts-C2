—------------------------------
# iOS Shortcuts C2
—------------------------------

Welcome, this project is dedicated to researching the iOS shortcuts application to discover vulberabilies for use to C2 most iOS devices using a mix of tools such as a custom SSH server, .shortcut files and keystroke injection to deliver a malicous shortcut file written to C2 iOS devices

## Context


Shortcuts is an application meant to help automate lots of functions within the OS of the device (iOS, iPadOS and MacOS) it can perform basic functions within the device using a node based system. This application runs with universal permissions giving it more access to certain information compared to other 3rd party applications.

Using keystroke injection, A user can deploy a malicious shortcut file to gather potential sensitive information and files from a device, some of the information that can be accessed from the shortcuts application is, GPS Coordinates, Parked car location, Networking information (Device and connected network), Full Contacts table (Numbers, Names, Emails, Addresses), and more

While some of this information (not all) requires a user to accept a prompt, this prompt does not require any authentication past physically touching the accept button. Making it easy to abuse using keystroke injection.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4cd86174-25b6-40bb-9d3f-c72b9dea60ee" alt="Image Description" width="300" height="auto">
</p>

With a few enabled settings Shortcuts is able to use SSH on the iPhone within its node language. This allows an attacker to use Shortcut variables and information within the SSH commands sent by the iPhones. This enables the ability to send possbily sensitive information over SSH. A modified SSH server allows an attacker to receive the commands from the device and then close the channel emulating a normal SSH server. While the Device believes it just ran a command on a SSH server it has sent sensitive data to the server and gotten back a predefined response from the modified SSH server. 

Attackers can also leverage SSH command output as a C2 functionality. A normal SSH server behaves `input command:whoami output: NAME` with a custom SSH server an attacker can specify the output `input command:whoami output: ATTACKER SPECIFIED OUTPUT`, 

the output can then be used as a variable within the node language used by shortcuts. For example `If SSH Has Does/Does Not Response: DEFINED ACTION`
<p align="center">
  <img src="https://github.com/user-attachments/assets/912d53d1-06e4-41a1-8dcf-dea5d57d40cd" alt="Image Description" width="300" height="auto">
</p>
This creates the opportunity to use SSH response as a command and control system. SSH responses can also be used as a string for the node language, for example `openlink: SSH RESPONSE`. 
<p align="center">
  <img src="https://github.com/user-attachments/assets/36abe184-7a63-4112-ba86-6a8ac94f4954" alt="Image Description" width="300" height="auto">
</p>

It is also possible to attach the malicious shortcut files to the automation function of shortcuts, this automates the process of running the file for certain actions for example, `when iMessages is opened: Run Malicious shortcut` enabling a level of presistance. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/ff09cce5-0d3d-4862-95db-e0eb35eb43c5" alt="Image Description" width="300" height="auto">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/53b2c751-efc5-4430-81a8-ba06927b42b4" alt="Image Description" width="300" height="auto">
</p>




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



