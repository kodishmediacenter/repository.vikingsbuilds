import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

#from addon.common.addon import Addon

#addonID = 'plugin.video.somlivre'
#addon   = Addon(addonID, sys.argv)
#local   = xbmcaddon.Addon(id=addonID)
icon    = "https://yt3.ggpht.com/a-/ACSszfGytKnwmNfEGexgHwk44SaxESMtQ2f1pBaTYw=s900-mo-c-c0xffffffff-rj-k-no"
base    = 'plugin://plugin.video.youtube/'


def run():
    plugintools.log("somlivre.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):

    
                
    


                
		plugintools.log("somlivre ===> " + repr(params))
                plugintools.add_item(title = "Som Livre"         , url = base + "channel/UCEATCATai_oafDuqKssZITw/playlists/",       thumbnail = icon, folder = True)
                
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')

run()

