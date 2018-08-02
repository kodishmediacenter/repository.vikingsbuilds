# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.espiritismo'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

icon1 = "https://yt3.ggpht.com/-Wn40S2a-C_M/AAAAAAAAAAI/AAAAAAAAAAA/UBHbhnJTLzc/s100-c-k-no/photo.jpg"
icon2 = "https://yt3.ggpht.com/-VoPMl_fmjZk/AAAAAAAAAAI/AAAAAAAAAAA/qrdvNb7qPeI/s100-c-k-no/photo.jpg"
icon3 = "https://yt3.ggpht.com/-T2FMRSsNMkQ/AAAAAAAAAAI/AAAAAAAAAAA/tHhx4SN4J3U/s100-c-k-no/photo.jpg"
icon4 = "https://yt3.ggpht.com/-xKVGOSYb53A/AAAAAAAAAAI/AAAAAAAAAAA/4cNBCiQF2uE/s100-c-k-no/photo.jpg"
icon5 = "https://yt3.ggpht.com/-5Z8a1eRRZuU/AAAAAAAAAAI/AAAAAAAAAAA/KIt0a4pjuX0/s100-c-k-no-rj-c0xffffff/photo.jpg"
icon6 = "https://yt3.ggpht.com/-A_cuKDfT3ek/AAAAAAAAAAI/AAAAAAAAAAA/25_CmJmQmIM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
icon7 ="https://yt3.ggpht.com/-tZb7spclwY4/AAAAAAAAAAI/AAAAAAAAAAA/M0cZxBeGHQQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
icon8 = "https://yt3.ggpht.com/-zu6Oy1uxa2E/AAAAAAAAAAI/AAAAAAAAAAA/HyW95ZndvWY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
icon9 = "https://yt3.ggpht.com/-3tM9qAKBcPU/AAAAAAAAAAI/AAAAAAAAAAA/OGur7_ZK5dk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
icon10= "http://2vi0v53jm68z12i7xp24npre1aqy.wpengine.netdna-cdn.com/wp-content/uploads/2014/04/livro-dos-espritos.jpg"
icon11= "http://3.bp.blogspot.com/-Gxvfik9olTw/U6MNs8FxkGI/AAAAAAAAApA/P3LVH_CkvT8/s1600/livro-dos-mediuns.png"
icon12= "http://sejoannadeangelis.org/site/wp-content/uploads/2016/02/17.jpg"
icon13= "http://www.ceoe.org.br/ceoe/images/2016/1631766_gr.jpg"
icon14= "http://www.caminhosdoamor.org.br/wp-content/uploads/2015/01/genese-allan-kardec.jpg"
icon15 = "http://4.bp.blogspot.com/-0LjJCuYO7-0/VB7HjxWa5uI/AAAAAAAAC5o/qBs5F6xZCkw/s1600/TUDO%2BDE%2BBOM%2BEM%2BAUDIOBOOK,%2BEBOOK%2BE%2BMAIS!.jpg"
def run():
    plugintools.log("espiritismo.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("espiritismo ===> " + repr(params))


                plugintools.add_item(title = "Programa Transição 1 temp"              , url = base + "playlist/PL5fdNclF-8A9Ck-pSCelBP-hgKiRiRJ8L/", thumbnail = icon, folder = True)
      

		plugintools.add_item(title = "Programa Transição 2 temp"              , url = base + "playlist/PL5fdNclF-8A_aYgztmrEeH6jcuIjUO4A-/", thumbnail = icon, folder = True)

                plugintools.add_item(title = "Programa Transição 3 temp"              , url = base + "playlist/PL5fdNclF-8A9Ssr1d8LmyWEBPJOPXTM5O/", thumbnail = icon, folder = True)
      
                plugintools.add_item(title = "Programa Transição 4 temp"              , url = base + "playlist/PL5fdNclF-8A8mJaFmsJLLc-0bL6Rv2XDn/", thumbnail = icon, folder = True)

                plugintools.add_item(title = "Espiritismo Esta na Biblia"              , url = base + "playlist/PL5fdNclF-8A-nL00dDFLQL3Ze5FE4FiAx/", thumbnail = icon, folder = True)

		plugintools.add_item(title = "Espiritismo Agora"       		       , url = base + "playlist/PL5fdNclF-8A9fGY1h2K30v0pcaJPWl0iw/", thumbnail = icon, folder = True)

		plugintools.add_item(title = "Deus Jesus e Caridade"       		, url = "plugin://plugin.video.youtube/user/samirjosebh/", thumbnail = icon, folder = True)

		plugintools.add_item(title = "Canal Amigos da Luz"    		        , url = base + "channel/UCYatoBlRirWhMrgjTK0b6Pg/", thumbnail = icon3, folder = True)
		
		plugintools.add_item(title = "Tv Mundo Maior"    		        , url = base + "channel/UCkrcoalvMERq3ehh5gH5j0Q/", thumbnail = icon2, folder = True)
		
		plugintools.add_item(title = "Canal Yeah "       		       , url = "plugin://plugin.video.youtube/user/yeahjovem/", thumbnail = icon1, folder = True)
		
		plugintools.add_item(title = "Canal FEB tv Brasil "       	       , url = "plugin://plugin.video.youtube/user/FEBtvBrasil/", thumbnail = icon4, folder = True)
		
		plugintools.add_item(title = "Tv Nova Luz"       	            , url = "plugin://plugin.video.youtube/user/DespertarEspirita/", thumbnail = icon5, folder = True)

		plugintools.add_item(title = "Filmáticas Espírita"       	            , url = base +  "channel/UCTu7wLVfJ0303dbkGGpRsFw/", thumbnail = icon6, folder = True)
        
		plugintools.add_item(title = "Palestra Espirita "       	            , url = base +  "user/PEspirita/", thumbnail = icon7, folder = True)
		
		plugintools.add_item(title = "Ensencia Espirita  "       	            , url = base +  "channel/UCv37nXNe2I2xseBE87GyLvQ/", thumbnail = icon8, folder = True)
		plugintools.add_item(title = "Luz do Espiritismo  "       	            , url = base +  "channel/UCXZf964iFfaIBjegUhMJ-1A/", thumbnail = icon9, folder = True)
		plugintools.add_item(title = "Livro do Espiritos (AudioBook)  "       	            , url = base +  "playlist/PLIe74p9kSlGax_0_OUPRiXIWXEIle1yD4/", thumbnail = icon10, folder = True)
		plugintools.add_item(title = "Livro O Evangelho Segundo Espiritismo  (AudioBook)  "       	            , url = base +  "playlist/PL-FWuois0pj5zzh2NqC2raID3-KYvZ268/", thumbnail = icon12, folder = True)
		plugintools.add_item(title = "Livro dos Mediuns  (AudioBook)  "       	            , url = base +  "playlist/PLkOfvAzyHuOAX7RpvrfD7sTXyaUvQLn4M/", thumbnail = icon11, folder = True)
		plugintools.add_item(title = "Ceu o Inferno  (AudioBook)  "       	            , url = base +  "playlist/PLkOfvAzyHuODfteeofnLHnUwbFZi47Vmj/", thumbnail = icon13, folder = True)
		plugintools.add_item(title = "A Genese       (AudioBook)  "       	            , url = base +  "playlist/PLi2zlDEJj-9EbhUOMi_42xOBeQYKrCWOH/", thumbnail = icon14, folder = True)
		plugintools.add_item(title = "Memorias de Suicida(AudioBook)  "    	            , url = base +  "playlist/PLkOfvAzyHuOBv1Qeknr01g65x5FDH6rlA/", thumbnail = icon15, folder = True)

		plugintools.add_item(title = "Musicas Espiritas"       	            , url = "plugin://plugin.video.youtube/user/jorgespontes/", thumbnail = icon, folder = True)


                plugintools.add_item(title = "Filmes Espiritas"       		       , url = base + "playlist/PLu1z7jY6SMvsEwxBJrhF3vPQrvgt-livt/", thumbnail = icon, folder = True)

                plugintools.add_item(title = "Filmes Espiritas 2"       		, url = base + "playlist/PLLrr0sD-lN7GJKIh8IQsyB7nortnRjoNW/", thumbnail = icon, folder = True)
      
      
		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
