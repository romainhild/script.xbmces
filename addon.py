import subprocess
import os
import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addonpath   = addon.getAddonInfo('path')
cmd         = addonpath + '/resources/lib/xbmces.sh'
 
ret = xbmcgui.Dialog().yesno(addonname, addon.getLocalizedString(32000))

if ret:
    devnull = open(os.devnull, 'wb')
    subprocess.Popen(["nohup", cmd], stdout=devnull, stderr=devnull)
