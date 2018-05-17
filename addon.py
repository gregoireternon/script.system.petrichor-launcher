import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "PETRICHOR"
line2 = "Use this add on to launch petrichor services"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)

