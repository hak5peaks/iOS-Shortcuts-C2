—------------------------------
# iOS C2 Documentation
## (REPO WILL BE CONTINUOUSLY UPDATED WITH NEW RESEARCH) 
—------------------------------

Welcome, this repo is for researching how iOS shortcuts application can be used to C2 most iOS devices using a mix of tools such as a custom SSH server, .shortcut files and keystroke injection to deliver a file and C2 iOS devices



# SSH Server Set Up

We are using a custom made SSH server to receive data from the iOS device using SSH. Using python and paramiko we have created a SSH server that does not serve a shell but however logs sent data from its users allowing us to use the SSH protocol to exfil data from the iOS Device

Setup is easy simply install the required packages 

> pip install requirements.txt
The SSH server will generate a host key if there is not one already.  it will use this key each time you start the server 


# iOS Shortcut Payload 

We are using a premade .shortcut file from another iOS device for the shortcut we will be using to gather information. These files are signed and has a Root CA certification that allow them to be download and ran with the shortcuts application 

![image](https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/d93f1553-7553-411d-a876-a404d95fc1ed)


This file should be downloaded onto the device and once opened should directly be imported to the Shortcuts application. 

# iOS Settings 

Once the file is imported and on the device we need to configure the iOS device to allow it to run the shortcut. Navigating to Settings -> Shortcuts -> Advanced we can find the setting to Allow Running Scripts, enabling this will allow us to run SSH scripts and run Javascript on websites from the Shortcuts App. Enabling Allow Sharing Large Amounts Of Data will also allow for large amounts of data to be sent over SSH 

![image](https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/62c9a031-f8be-4dd0-ad6b-a86dd8159a56)



#Connecting Shortcuts to Automations 

To enable the shortcut to act as a logic bomb or even run it as a loop we will need to connect the shortcut to a automation 

There are several different trigger options for Automations

![image](https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/23e5ee5b-5413-4d6c-b217-2167746b69b9)
![image](https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/d0cc33e0-fc41-49a5-889e-bb97317fa0fe)
![image](https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/8ea993a6-65c4-442f-a967-a3b60569d8fe) 

Once a trigger is selected and configured and we are inside the action menu we will want to add a “Run Shortcut” action so once the automation is ran it will run our shortcut 

![image](https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/a8defb14-1990-4082-95dc-722b8805a20f)

Once we complete setting up the shortcut we will want to disable ask before running and notify when ran this will help in keeping the shortcut hidden on the device, keep in mind some automation triggers do not allow you to turn these settings off such as Message and email 

![image](https://github.com/Peaakss/iOS-C2-BETA/assets/115900893/9df12376-29d7-45f2-bf9a-b3e2074a8045)

# More context 

Ideally to deliver and run our shortcut we will want to have a custom web server hosting our .shortcut file. It is possible to do use all by hand with physical unlocked access to the device, however we can use keystroke injection to automate and speed up the process using a device like the O.MG cable 



