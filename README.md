—------------------------------
# iOS Shortcuts C2
—------------------------------

## Context

"Shortcuts" is an application within the Apple ecosystem meant to help automate lots of functions within the OS of devices (iOS, iPadOS, visionOS, MacOS). It can perform basic functions within the device using a node based programming system. 

Using physical, unlocked access, a user can deploy a malicious shortcut file to gather potentially sensitive information and files from a device, including things such as GPS Coordinates, Parked car location, Networking information (Device and connected network), Full Contacts table (Numbers, Names, Emails, Addresses). These are all easily obtainable, and deployment speed can optimized utilizing keystroke injection tools such as the Hak5 Rubber Ducky or the O.MG cable. 

Certain types of information requires a user to accept a prompt, however this prompt does not require any authentication past physically touching the accept button. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/4cd86174-25b6-40bb-9d3f-c72b9dea60ee" alt="Image Description" width="300" height="auto">
</p>

With a few enabled settings, Shortcuts is able to use the SSH client on the iPhone within its node language. This allows the use of Shortcut variables and information within the SSH commands sent by iPhones. This enables the ability to send potentially sensitive information over SSH. This information can be collected ultizing a custom SSH server. 
`Settings -> Shortcuts -> Advanced -> Allow Running Scripts`

<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/62c9a031-f8be-4dd0-ad6b-a86dd8159a56" alt="Image Description" width="500" height="auto">
</p>

Shortcuts can also leverage SSH command outputs as node instructions. This allows Shortcuts to use the output from the remote SSH server to determine further instructions. 

A normal SSH server behaves like so:
`input command:whoami output: NAME` 
While with a custom SSH server, an attacker can specify the output
`input command:whoami output: ATTACKER SPECIFIED OUTPUT` 

This output can then be used as a variable within the node language used by shortcuts. For example `If SSH Has Does/Does Not Response: DEFINED ACTION`
<p align="center">
  <img src="https://github.com/user-attachments/assets/912d53d1-06e4-41a1-8dcf-dea5d57d40cd" alt="Image Description" width="300" height="auto">
</p>

This creates the opportunity to use SSH responses as a command and control system. SSH responses can also be used as a string for the node language, for example `openlink: SSH RESPONSE` 

<p align="center">
  <img src="https://github.com/user-attachments/assets/36abe184-7a63-4112-ba86-6a8ac94f4954" alt="Image Description" width="300" height="auto">
</p>

It is also possible to attach malicious shortcut files to the automation function of shortcuts, this automates the process of running the file for certain actions, for example, `when iMessages is opened: Run Malicious shortcut` enabling a level of presistence. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/ff09cce5-0d3d-4862-95db-e0eb35eb43c5" alt="Image Description" width="300" height="auto">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/53b2c751-efc5-4430-81a8-ba06927b42b4" alt="Image Description" width="300" height="auto">
</p>

# Apple declared this research a non-security issue as of 2/24/24, 3:50 PM

<p align="center">
<img src="https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/483212b1-8b66-4eb8-8880-89fdeb823347" alt="Image Description" width="500" height="auto">
</p>
