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



# Apple has declared this research a non-security issue as of 2/24/24, 3:50 PM

<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/483212b1-8b66-4eb8-8880-89fdeb823347" alt="Image Description" width="500" height="auto">
</p>

# iOS Settings 

Once the file is imported and on the device we need to configure the iOS device to allow it to run the shortcut. Navigating to Settings -> Shortcuts -> Advanced we can find the setting to Allow Running Scripts, enabling this will allow us to run SSH scripts and run Javascript on websites from the Shortcuts App. Enabling Allow Sharing Large Amounts Of Data will also allow for large amounts of data to be sent over SSH 
<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/62c9a031-f8be-4dd0-ad6b-a86dd8159a56" alt="Image Description" width="500" height="auto">
</p>




