# Kodi Add-on xbmces

This add-on allows to stop Kodi and launch EmulationStation. And once EmulationStation quits, relaunch Kodi.

You need to have EmulationStation installed on your system.
This is for Linux, and has been tested on a raspberry pi via Xbian.

## Miscellaneous

You need to edit your sudoers fils so you don't need to enter your password for the `service` command:
```
user ALL = (root) NOPASSWD: /usr/bin/service
```
