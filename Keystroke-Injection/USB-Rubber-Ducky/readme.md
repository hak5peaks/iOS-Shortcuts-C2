# Hak5 USB rubber ducky payload 

This payload is written and deployed using the official Hak5 USB rubber ducky, This payload is designed to quickly configure and deploy SSH shortcuts on iOS devices. Tested on iPhone 15 pro max, iOS Verison 17.6.1

# Configuration

Lines 38 and 39 need to be changed to your shortcut share link and shortcut name.

```
DEFINE #SHORTCUT_URL shortcuts://shortcuts/(PLACE YOUR SHORTCUT ID HERE)
DEFINE #SHORTCUT_NAME placeholder

REM for example: #URL shortcuts://shortcuts/000000000000000000
REM for example: #URL shortcuts://shortcuts/Shortcut.name
```
