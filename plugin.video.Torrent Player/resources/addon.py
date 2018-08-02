#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,sys
import time,subprocess,webbrowser,sys
import urlresolver
from BeautifulSoup import BeautifulSoup


addon_base = 'Torrent Player'
addon_id = 'plugin.video.Torrent Player'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
PROXIMA_PAGINAS = addonfolder + '/resources/img/download.png'
fanart = addonfolder + '/fanart.jpg'
icones = addonfolder + '/icon.png'
base = 'http://forumchaves.com.br/listach/site/lista.php'
base2 = 'http://www.kboing.com.br'
dialog=xbmcgui.Dialog()


############################################################################################################
#                                           MENU ADDON                                                 
############################################################################################################

def CATEGORIES():
	addDir('THE PIRATE FILMES HD','-',1,artfolder+'THEPIRATEFILMESHD.png')
	addDir('COMANDO TORRENTS','-',1,artfolder+'Comando Torrents.png')
	#addDir('4K-FILMES','-',1,artfolder+'4K17.png')
	addDir('TEU TORRENT','-',1,artfolder+'TeuTorrent.png')
	addDir('TORRENTOON','-',1,artfolder + 'Torrentoon.png')
	addDir('LAPUMIA FILMES','-',1,artfolder + 'LAPUMiA FiLMES.png')


###################################################################################
#FUNCOES

'''
algerian,castellar,colonna Mt,Imprint MT shadow
urllib.unquote(urllib.unquote(urllib.unquote(urllib.unquote(urllib.unquote(urls)))))
'''		

def menu_sites(name):
	if 'THE PIRATE FILMES HD'==name:
		addDir('LANÇAMENTOS','http://www.thepiratefilmeshd.com/',2,iconimage)
		addDir('SERIES','http://www.thepiratefilmeshd.com/category/series/',2,iconimage)
		addDir('CATEGORIAS','http://www.thepiratefilmeshd.com/',4,iconimage)
		addDir('PESQUISA','-',5,iconimage)	
	if 'COMANDO TORRENTS'==name:
		addDir('LANÇAMENTOS','http://www.comandotorrents.com/',6,iconimage)
		addDir('SERIES','http://www.comandotorrents.com/category/series/',6,iconimage)
		addDir('CATEGORIAS','http://www.comandotorrents.com/',8,iconimage)
		addDir('ANO','http://www.comandotorrents.com/',9,iconimage)
		addDir('FORMATOS','http://www.comandotorrents.com/',11,iconimage)
		addDir('PESQUISA','-',10,iconimage)	
	if '4K-FILMES'==name:
		addDir('LANÇAMENTOS','http://4k-filmes.com/',12,iconimage)
		addDir('CATEGORIAS','http://4k-filmes.com/',14,iconimage)
		addDir('UPLOADERS','http://4k-filmes.com/',15,iconimage)
		addDir('PESQUISA','-',16,iconimage)	
	if 'TEU TORRENT'==name:
		addDir('LANÇAMENTOS','http://teutorrent.com/category/lancamentos/',17,iconimage)
		addDir('CATEGORIAS','http://teutorrent.com/category/lancamentos/',19,iconimage)
		addDir('PESQUISA','-',20,iconimage)	
	if 'TORRENTOON'==name:
		addDir('LANÇAMENTOS','http://torrentoon.com/lancamentos',21,iconimage)
		addDir('FILMES','http://torrentoon.com/filmes',21,iconimage)
		addDir('DESENHOS','http://torrentoon.com/desenhos',21,iconimage)
		addDir('SERIES','http://torrentoon.com/series',21,iconimage)
		addDir('CATEGORIAS FILMES','http://torrentoon.com/',24,iconimage)
		addDir('CATEGORIAS DESENHOS','http://torrentoon.com/',25,iconimage)
		addDir('CATEGORIAS SERIES','http://torrentoon.com/',26,iconimage)
		addDir('PESQUISA','-',23,iconimage)		
	if 'LAPUMIA FILMES'==name:
		addDir('LANÇAMENTOS','http://www.lapumiafilmes.com/',27,iconimage)
		addDir('CATEGORIAS','http://www.lapumiafilmes.com/',29,iconimage)
		addDir('PESQUISA','-',30,iconimage)	
def cleanTitle(title):
    title = title.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&#038;", "&").replace("&#39;", "'")
    title = title.replace("&#039;", "'").replace("&#8211;", "-").replace("&#8220;", "-").replace("&#8221;", "-").replace("&#8217;", "'")
    title = title.replace("&quot;", "\"").replace("&uuml;", "ü").replace("&auml;", "ä").replace("&ouml;", "ö")
    title = title.strip()
    return title
	
def extract_magnets(data):
    import re
    for magnet in re.findall(r'magnet:\?[^\'"\s<>\[\]]+', data):
        yield {"uri": magnet}		
	
###################################################################################
'''
									LAPUMIAFILMES 	INICIO
'''
###################################################################################	   lapumiafilmes_pegar_pesquisa 
def clean_name2(name):
	name = name.replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','')
	return name



	
def lapumiafilmes_pegar_categorias(url):
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile('<li id="menu-item-.*?" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.*?"><a href="(.*?)">(.*?)</a></li>').findall(link)
	for url,name in reg:
		name= clean_name(name)
		addDir(name,url,27,iconimage)		
		
	
	
def lapumiafilmes_pegar_links(url):
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	#reg = re.compile('<strong style="box-sizing:.*?">.*?</strong></span><a href="(.*?)"><img class="aligncenter" src=".*?" data-lazy-src="//.*?').findall(link)
	for url in reg:
		if 'magnet:?xt=' in url:
			name = url.split('dn=')[-1].split('tr=')[0]
			name = urllib.unquote_plus(name).replace('Audio-BLUDV.COM','').replace('.Amazon.WEB-DL.Dual ','').replace('','')
			name = clean_name(name)
			addDir(name,url,99,iconimage)		

'''	reg = re.compile('<div style="text-align:.*?">.*?Epis.*?dio.*? <a href="(.*?)">.*?</a>').findall(link)
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	for url in reg:
		if 'magnet:?xt=' in url:
			name = url.split('dn=')[-1].split('tr=')[0]
			name = urllib.unquote_plus(name).replace('Audio-BLUDV.COM','').replace('.Amazon.WEB-DL.Dual ','').replace('','')
			name= clean_name(name)
			addDir(name,url,99,iconimage)	
			
	#reg = re.compile('<div style="text-align: center;">.*?Cap.*?tulo.*?<a href="(.*?)">.*?</a></div>').findall(link)
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	for url in reg:
		if 'magnet:?xt=' in url:
			name = url.split('dn=')[-1].split('tr=')[0]
			name = urllib.unquote_plus(name).replace('Audio-BLUDV.COM','').replace('.Amazon.WEB-DL.Dual ','').replace('','')
			name= clean_name(name)
			addDir(name,url,99,iconimage)'''				
	
def lapumiafilmes_pegar_pesquisa():
    keyb = xbmc.Keyboard('', 'Faca sua Busca...')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
        url = 'http://www.lapumiafilmes.com/?s='+parametro_pesquisa
        lapumiafilmes_pegar_videosss(url)


	
			
def lapumiafilmes_pegar_videosss(url):
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('<h2 class="bg-post-blog">\s*<a href="(.*?)" rel="bookmark" title="(.*?)">.*?<noscript><img title=".*?" src="(.*?)" alt="').findall(link)
	for url,name,img in reg:
		name = clean_name2(name).replace(' Torrent',' ')
		name = name.split(' – ')[0].split('  - ')[0].split(' Torent - ')[0]
		img = img.replace('//','http://')
		name = name.replace('#8211;','').replace('amp;','').replace('&','').replace('','').replace('','').replace('','').split('   ')[0]
		addDir(name,url,999,img)		#28
		
	reg = re.compile('<span class=\'current\'>(.*?)</span><a class="page larger" title="Page.*?" href="(.*?)">.*?</a>').findall(link)
	for essa,proxima_pagina in reg:
		pro = int(essa)+1
		addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),proxima_pagina,31,PROXIMA_PAGINAS)	
			
def lapumiafilmes_pegar_videos(url):
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('<div class="titulo-post"><h2 class="bg-post-blog"> <a href="(.*?)" rel="bookmark" title=".*?">.*?</a></h2></div><div class="infos">.*?<img title=".*?" src=".*?" data-lazy-src="(.*?)" alt="(.*?)" width=".*?" border="0" />').findall(link)
	for url,img,name in reg:
		name = clean_name2(name).replace(' Torrent',' ')
		name = name.split(' – ')[0].split('  - ')[0].split(' Torent - ')[0]
		img = img.replace('//','http://')
		addDir(name,url,999,img)		#28
		
	reg = re.compile('<span class=\'current\'>(.*?)</span><a class="page larger" title="Page.*?" href="(.*?)">.*?</a>').findall(link)
	for essa,proxima_pagina in reg:
		pro = int(essa)+1
		addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),proxima_pagina,27,PROXIMA_PAGINAS)	

###################################################################################
'''
									LAPUMIAFILMES 	FIM
'''
###################################################################################	
############################################################################################################################################################		
###################################################################################
'''
									TORRENTOON 	INICIO
'''
###################################################################################	  
	
	
def clean_name(name):
	name = name.replace('#038;','').replace('amp;','').replace('&','').replace('WWW.BLUDV.COM','').replace(' [BluRay] ',' ').replace(' IMAX ',' ').replace(' [720p] ',' ').replace('- WWW.',' ').replace('TORRENTBRAZIL.ORG','').replace('-BLACKOUT','').replace('.Nacional','').replace('.AC3','').replace('.DVDRip','').replace(' Torrent ',' ').replace(' Download ',' ').replace('– WEB-DL ',' ').replace(' 720p e 1080p ',' ').replace(' BluRay ',' ').replace('– Dublado ',' ').replace('#8211;','').replace(' WEBRip ',' ').replace(' Dual Áudio',' ').replace('  / ',' ').replace(' / ',' ').replace('  Legendado',' ').replace(' Legendado',' ').replace(' – 5.1',' ').replace(' 1080p ',' ').replace(' WEB-DL ',' ').replace(' Dublado ',' ').replace(' 5.1 ',' ').replace(' REMASTERIZADO ',' ').replace(' HDTV ',' ').replace(' – ',' ').replace(' 720p ',' ').replace(' – ',' ').replace('#8217;','').replace(' Download',' ').replace(' | ',' ').replace(' HDRip ',' ').replace(' e ',' ').replace('.x264-GECKOS',' ').replace('.H264.AAC-RARBG',' ').replace('.PROPER',' ').replace('.WWW.COMANDOTORRENTS.COM',' ').replace('.DD5.1.x264-DUAL ',' ').replace('[COMANDOTORRENTS.COM] ',' ').replace('.ENG.X264-Feel.Free',' ').replace(' COMANDOTORRENTS.COM',' ').replace('.x264-REGARDS',' ').replace('.x264-FGT',' ').replace('.DD5.1.H264-FGT',' ').replace('.XviD-FGT',' ').replace('.HC.HDRip.X264-DUAL ',' ').replace(' COMANDOTORRRENTS.COM',' ').replace('.x264-DUAL ',' ').replace('.FULL','').replace('.x264-BiPOLAR',' ').replace('.BDRip ',' ').replace('.x264-VALUE',' ').replace(' x264-JellyBean',' ').replace('-WWW.COMANDOTORRENTS.COM',' ').replace('TS.x264.',' ').replace('.1920X1080.NonDRM_[FHD].mp4',' ').replace('.H264.AAC-CJCONTENTS.mp4',' ').replace(' x264 AC3 Line DUAL ',' ').replace('.XviD.MP3-RARBG',' ').replace('.x264-VETO',' ').replace('.x264.TiTAN',' ').replace('.X264-AMIABLE',' ').replace('.x264.DTS-DUAL ',' ').replace('.x264.HORiZON-ArtSubs',' ').replace('.HDRip.XviD-EVO',' ').replace('.x264-SVA','').replace('.REPACK',' ').replace('.XviD.MP3-FGT',' ').replace('.x264-DRONES',' ').replace('- MKvCage',' ').replace('.x264-Grym',' ').replace('.COMANDOTORRENTS.COM',' ').replace('-COMANDOTORRENTS.COM',' ').replace('.HDTV.x264','.HDTV').replace(' Baixar ',' ').replace(' |   ',' ').replace(' |  ',' ').replace(' |1080p  ',' ').replace(' Leg',' ').replace(' Dub ',' ').replace(' Blu-Ray ',' ').replace(' Dublado',' ').replace(' (2017) ',' ').replace(' #Desafio Mundial ',' ').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('Audio-BLUDV.COM','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','')
	return name			
	
	
def torrentoon_pegar_categorias_series(url):#titled  teutorrent_pegar_pesquisa  http://teutorrent.com/?s=LOgan&tipo=audio
	link = abrir_url(url).replace('\n','').replace('\r','')
	link = re.findall('<li><a href="series" title="Séries Torrent Assistir Online">Séries</a><ul>(.*?)<li><a href="jogos" title="Jogos Torrent Assistir">Jogos</a><ul>',link)[0]
	reg = re.compile('<li><a href="(.*?)" title=".*?">(.*?)</a></li>').findall(link)
	for url,name in remove_repetidos(reg):
		base = 'http://torrentoon.com/'
		addDir(name,base+url,21,'')	
		

	
def torrentoon_pegar_categorias_desenhos(url):#titled  teutorrent_pegar_pesquisa  http://teutorrent.com/?s=LOgan&tipo=audio
	link = abrir_url(url).replace('\n','').replace('\r','')
	link = re.findall('<li><a href="desenhos" title="Desenhos Animados Torrent Assistir Online">Desenhos</a><ul>(.*?)<li><a href="series" title="Séries Torrent Assistir Online">Séries</a><ul>',link)[0]
	reg = re.compile('<li><a href="(.*?)" title=".*?">(.*?)</a></li>').findall(link)
	for url,name in remove_repetidos(reg):
		base = 'http://torrentoon.com/'
		addDir(name,base+url,21,'')	
		

	
def torrentoon_pegar_categorias(url):#titled  teutorrent_pegar_pesquisa  http://teutorrent.com/?s=LOgan&tipo=audio
	link = abrir_url(url).replace('\n','').replace('\r','')
	link = re.findall('<li id="filmesd">(.*?)<li><a href="desenhos" title="Desenhos Animados Torrent Assistir Online">Desenhos</a><ul>',link)[0]
	reg = re.compile('<li><a href="(.*?)" title=".*?">(.*?)</a></li>').findall(link)
	for url,name in remove_repetidos(reg):
		base = 'http://torrentoon.com/'
		addDir(name,base+url,21,'')	
		


def torrentoon_pegar_pesquisa():
    keyb = xbmc.Keyboard('', 'Faca sua Busca...')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
        url = 'http://torrentoon.com/index.php?palavra='+parametro_pesquisa+'&envia=Buscar'
        storrentoon_pegar_videos(url)

		
def storrentoon_pegar_videos(url):#titled  thepiratefilmeshd_pegar_links  
	link = abrir_url(url).replace('\n','').replace('\r','')
	base = 'http://torrentoon.com/'
	reg = re.compile('<div class="post_img2"><a href="(.*?)"><img src="(.*?)" width=".*?" title="(.*?)" alt=".*?">').findall(link)
	for url,img,name in reg:
		name = clean_name(name).replace(' Torrent',' ')
		addDir(name,base+url,999,img)	#	
	reg = re.compile('<div class="capa_media">\s*<a href="(.*?)"><img src="(.*?)"  alt=".*?" title="(.*?)"></a>').findall(link)
	for url,img,name in reg:
		name = clean_name(name).replace(' Torrent',' ')
		addDir(name,base+url,999,img)	#	
		
	if 'pagina_atual' in link:
		reg = re.compile('<div class=\'pagina_atual\'>(.*?)</div><a href="(.*?)" title=".*?">').findall(link)
		for essa,proxima_pagina in reg:
			pro = int(essa)+1
			addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),base+proxima_pagina,21,PROXIMA_PAGINAS)	
	else:
		reg = re.compile('<a href="filmes-.*?" title="Primeira Página">Primeira página</a><a href="(.*?)" title="Próxima Página">Próxima Página</a></div><!--<div id="fb-root"></div>').findall(link)
		for proxima_pagina in reg:
			addDir('Próxima Página',base+proxima_pagina,21,PROXIMA_PAGINAS)	


def torrentoon_pegar_links(url):#titled   torrentoon_pegar_pesquisa
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	#reg = re.compile('<a href="(.*?)" rel="nofollow" onclick=".*?"><img src=".*?" title="').findall(link)
	for url in reg:
		if 'magnet:?xt=' in url:
			name = url.split('dn=')[-1].split('tr=')[0]#"magnet:?xt=
			url = url.split('"magnet:?xt=')[-1]
			name = urllib.unquote_plus(name).replace('Audio-BLUDV.COM','').replace('.Amazon.WEB-DL.Dual ','').replace('','')
			name= clean_name(name)
			addDir(name,'magnet:?xt='+url,99,iconimage)		
'''	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
#	reg = re.compile('<div style="text-align:.*?"><a href="(.*?)"><img class="alignnone" src=').findall(link)
	for url in reg:
		if 'magnet:?xt=' in url:
			name = url.split('dn=')[-1].split('tr=')[0]
			name = urllib.unquote_plus(name)
			name= clean_name(name)
			addDir(name,url,99,iconimage)'''	
			


			

def torrentoon_pegar_videos(url):#titled  thepiratefilmeshd_pegar_links  
	link = abrir_url(url).replace('\n','').replace('\r','')
	base = 'http://torrentoon.com/'
	reg = re.compile('</span><a href="(.*?)"><img src="(.*?)"  alt=".*?" title="(.*?)"></a>').findall(link)
	for url,img,name in reg:
		name = clean_name(name).replace(' Torrent',' ')
		addDir(name,base+url,999,img)	#22	
	reg = re.compile('<div class="capa_media">\s*<a href="(.*?)"><img src="(.*?)"  alt=".*?" title="(.*?)"></a>').findall(link)
	for url,img,name in reg:
		name = clean_name(name).replace(' Torrent',' ')
		addDir(name,base+url,999,img)		#22
		
	if 'pagina_atual' in link:
		reg = re.compile('<div class=\'pagina_atual\'>(.*?)</div><a href="(.*?)" title=".*?">').findall(link)
		for essa,proxima_pagina in reg:
			pro = int(essa)+1
			addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),base+proxima_pagina,21,PROXIMA_PAGINAS)	
	else:
		reg = re.compile('<a href="filmes-.*?" title="Primeira Página">Primeira página</a><a href="(.*?)" title="Próxima Página">Próxima Página</a></div><!--<div id="fb-root"></div>').findall(link)
		for proxima_pagina in reg:
			addDir('Próxima Página',base+proxima_pagina,21,PROXIMA_PAGINAS)	

		
###################################################################################
'''
									TORRENTOON 	FIM
'''
###################################################################################	
############################################################################################################################################################		
###################################################################################
'''
									TEUTORRENT 	INICIO
'''
###################################################################################	

	
def clean_name(name):
	name = name.replace('#038;','').replace('amp;','').replace('&','').replace('WWW.BLUDV.COM','').replace(' [BluRay] ',' ').replace(' IMAX ',' ').replace(' [720p] ',' ').replace('- WWW.',' ').replace('TORRENTBRAZIL.ORG','').replace('-BLACKOUT','').replace('.Nacional','').replace('.AC3','').replace('.DVDRip','').replace(' Torrent ',' ').replace(' Download ',' ').replace('– WEB-DL ',' ').replace(' 720p e 1080p ',' ').replace(' BluRay ',' ').replace('– Dublado ',' ').replace('#8211;','').replace(' WEBRip ',' ').replace(' Dual Áudio',' ').replace('  / ',' ').replace(' / ',' ').replace('  Legendado',' ').replace(' Legendado',' ').replace(' – 5.1',' ').replace(' 1080p ',' ').replace(' WEB-DL ',' ').replace(' Dublado ',' ').replace(' 5.1 ',' ').replace(' REMASTERIZADO ',' ').replace(' HDTV ',' ').replace(' – ',' ').replace(' 720p ',' ').replace(' – ',' ').replace('#8217;','').replace(' Download',' ').replace(' | ',' ').replace(' HDRip ',' ').replace(' e ',' ').replace('.x264-GECKOS',' ').replace('.H264.AAC-RARBG',' ').replace('.PROPER',' ').replace('.WWW.COMANDOTORRENTS.COM',' ').replace('.DD5.1.x264-DUAL ',' ').replace('[COMANDOTORRENTS.COM] ',' ').replace('.ENG.X264-Feel.Free',' ').replace(' COMANDOTORRENTS.COM',' ').replace('.x264-REGARDS',' ').replace('.x264-FGT',' ').replace('.DD5.1.H264-FGT',' ').replace('.XviD-FGT',' ').replace('.HC.HDRip.X264-DUAL ',' ').replace(' COMANDOTORRRENTS.COM',' ').replace('.x264-DUAL ',' ').replace('.FULL','').replace('.x264-BiPOLAR',' ').replace('.BDRip ',' ').replace('.x264-VALUE',' ').replace(' x264-JellyBean',' ').replace('-WWW.COMANDOTORRENTS.COM',' ').replace('TS.x264.',' ').replace('.1920X1080.NonDRM_[FHD].mp4',' ').replace('.H264.AAC-CJCONTENTS.mp4',' ').replace(' x264 AC3 Line DUAL ',' ').replace('.XviD.MP3-RARBG',' ').replace('.x264-VETO',' ').replace('.x264.TiTAN',' ').replace('.X264-AMIABLE',' ').replace('.x264.DTS-DUAL ',' ').replace('.x264.HORiZON-ArtSubs',' ').replace('.HDRip.XviD-EVO',' ').replace('.x264-SVA','').replace('.REPACK',' ').replace('.XviD.MP3-FGT',' ').replace('.x264-DRONES',' ').replace('- MKvCage',' ').replace('.x264-Grym',' ').replace('.COMANDOTORRENTS.COM',' ').replace('-COMANDOTORRENTS.COM',' ').replace('.HDTV.x264','.HDTV').replace(' Baixar ',' ').replace(' |   ',' ').replace(' |  ',' ').replace(' |1080p  ',' ').replace(' Leg',' ').replace(' Dub ',' ').replace(' Blu-Ray ',' ').replace(' Dublado',' ').replace(' (2017) ',' ').replace(' #Desafio Mundial ',' ').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','')
	return name		

	


def teutorrent_pegar_pesquisa():
    keyb = xbmc.Keyboard('', 'Faca sua Busca...')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
        url = 'http://teutorrent.com/?s='+parametro_pesquisa
        teutorrent_pegar_videos(url)
	
	
def teutorrent_pegar_categorias(url):#titled  teutorrent_pegar_pesquisa  http://teutorrent.com/?s=LOgan&tipo=audio
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('<li class="cat-item.*?"><a href="(.*?)" >(.*?)</a>\s*(.*?)\s*</li>').findall(link)
	for url,name,ites in remove_repetidos(reg):
		if '/category/' in url:
			addDir(name+'  -  '+ites,url,17,'')		
			
		

def teutorrent_pegar_links(url):#titled
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	#reg = re.compile('<a href="(.*?)"><img class=".*?" src=').findall(link)
	for url in reg:
		if 'magnet:?xt=' in url:
			name = url.split('dn=')[-1].split('tr=')[0]
			name = urllib.unquote_plus(name)
			name= clean_name(name)
			addDir(name,url,99,iconimage)		
'''	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	#reg = re.compile('<li class="tooltip2" title=.*?<a href="(.*?)" target="_blank"><span name=').findall(link)
	for url in reg:
		if 'magnet:?xt=' in url:
			name = url.split('dn=')[-1].split('tr=')[0]
			name = urllib.unquote_plus(name)
			name= clean_name(name)
			addDir(name,url,99,iconimage)'''		


			
def teutorrent_pegar_videos(url):#titled  teutorrent_pegar_links
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('<div class="capa">\s*<a href="(.*?)" class="absolute-capa  no-text">(.*?)</a>.*?<img src="(.*?)".*?/>').findall(link)
	for url,name,img in reg:
		name = clean_name(name)
		addDir(name,url,999,img)	#18	
	reg = re.compile("<span aria-current='page' class='page-.*?'>(.*?)</span>\s*<a class='page-numbers' href='(.*?)'>.*?</a>").findall(link)
	for essa,proxima_pagina in reg:
		pro = int(essa)+1
		addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),proxima_pagina,17,PROXIMA_PAGINAS)	
	
###################################################################################
'''
									TEUTORRENT 	FIM
'''
###################################################################################	
############################################################################################################################################################
###################################################################################
'''
									4K17 	INICIO
'''
###################################################################################		



def _4k17_pegar_pesquisa():
    keyb = xbmc.Keyboard('', 'Faca sua Busca...')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
        url = 'http://4k-filmes.com/?s='+parametro_pesquisa
        _4k17_pegar_videos(url)

	
def _4k17_pegar_Uploaders():#titled
	addDir('Lucas Firmo','http://4k17.me/author/lucasfirmo62',12,'')		
	addDir('Belex','http://4k17.me/author/belex',12,'')		
	addDir('Lipeh','http://4k17.me/author/lipeh9',12,'')		
	addDir('Kleyson Lima','http://4k17.me/author/kleyson',12,'')		
	addDir('Legenda Oficial','http://4k17.me/author/legenda-oficial',12,'')		
	
def _4k17_pegar_categorias(url):#titled
	links = abrir_url(url).replace('\n','').replace('\r','')
	link = re.findall('<div id="subnavbar">(.*?)<div class="center">',links)[0]
	reg = re.compile("<li class='cat-item'>\s*<a href='(.*?)' title='.*?'>(.*?)</a></li").findall(link)
	#for url,name in remove_repetidos(reg):
	for url,name in reg:
		if not 'Jogos' in name:
			if '/category/' in url:
				addDir(name,url,12,'')		

				

def _4k17_pegar_videos(url):#titled  _4k17_pegar_links
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('</div><div class="center-widget-title"></div><div class="center-widget"><h2 class="post-title">\s*<a href="(.*?)" rel="bookmark" title=.*?>(.*?)</a>.*?<img src="(.*?)" alt=".*?" width=".*?" height=".*?" border=".*?" />').findall(link)
	for url,name,img in reg:
		name = clean_name(name)
		img = img.replace('//','http://')
		addDir(name,url,999,img)		#13
	reg = re.compile('<span class=\'current\'>(.*?)</span><a class="page larger" title="Page.*?" href="(.*?)">.*?</a>').findall(link)
	for essa,proxima_pagina in reg:
		pro = int(essa)+1
		addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),proxima_pagina,12,PROXIMA_PAGINAS)	

def _4k17_pegar_links(url):#titled
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	#reg = re.compile('<a href="magnet:(.*?)"><img class="aligncenter" src=.*?data-lazy-src=').findall(link)
	for url in reg:
		name = url.split('dn=')[-1].split('tr=')[0]
		name = urllib.unquote_plus(name)
		name= clean_name(name)
		#addDir(name,'magnet:'+url,99,iconimage)		
		addDir(name,url,99,iconimage)		
'''	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	reg = re.compile('<p style="text-align:.*?<a href="magnet:(.*?)">.*?</a>').findall(link)
	for url in reg:
		name = url.split('dn=')[-1].split('tr=')[0]
		name = urllib.unquote_plus(name)
		name= clean_name(name)
		addDir(name,url,99,iconimage)	
		#addDir(name,'magnet:'+url,99,iconimage)'''	
		
###################################################################################
'''
									4K17 	FIM
'''
###################################################################################	
############################################################################################################################################################################################################
###################################################################################
'''
									BLUDV 	INICIO
'''
###################################################################################		
		
	

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l



def comandotorrents_pegar_pesquisa():
    keyb = xbmc.Keyboard('', 'Faca sua Busca...')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
        url = 'http://www.comandotorrents.com/?s='+parametro_pesquisa
        comandotorrents_pegar_videos(url)


	
def comandotorrents_pegar_categorias(url):#titled
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('<h2><a href="(.*?)">(.*?)</a></h2>').findall(link)
	for url,name in remove_repetidos(reg):
		if '/category/' in url:
			addDir(name,url,6,'')		
			
			
def comandotorrents_pegar_foramtos(url):#titled 
	addDir('1080p','http://www.comandotorrents.com/category/1080p',6,'')	
	addDir('720p','http://www.comandotorrents.com/category/720p',6,'')	
	addDir('3D','http://www.comandotorrents.com/category/3d',6,'')	
	addDir('4k','http://www.comandotorrents.com/category/4k',6,'')	
	addDir('5.1','http://www.comandotorrents.com/category/5-1',6,'')	
	
	
	
def comandotorrents_pegar_ano(url):#titled <a href="http://www.comandotorrents.com/category/1080p/" rel="category tag">1080p</a>
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('nbsp;<a href="(.*?)">(.*?)</a>').findall(link)
	for url,name in reg:
		if '/category/' in url:
			addDir(name,url,6,'')		

	
		
def comandotorrents_pegar_videos(url):#titled
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('<h2 class="entry-title" itemprop="headline">\s*<a href="(.*?)">(.*?)</a></h2>.*?<img class=.*?data-lazy-src="(.*?)"').findall(link)
	for url,name,img in reg:
		name = clean_name(name)#7
		addDir(name,url,999,img)		
	reg = re.compile('<span class=\'current\'>(.*?)</span><a class="page larger" title="Page.*?" href="(.*?)">.*?</a>').findall(link)
	for essa,proxima_pagina in reg:
		pro = int(essa)+1
		addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),proxima_pagina,6,PROXIMA_PAGINAS)	



		
def comandotorrents_pegar_links(url):#titled
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	#reg = re.compile('<a href="magnet:(.*?)"><img class="aligncenter" src=.*?data-lazy-src=').findall(link)
	for url in reg:
		name = url.split('dn=')[-1].split('tr=')[0]
		name = urllib.unquote_plus(name)
		name= clean_name(name)
		addDir(name,url,99,iconimage)		
		#addDir(name,'magnet:'+url,99,iconimage)		
'''	reg = re.compile('<p style="text-align:.*?<a href="magnet:(.*?)">.*?</a>').findall(link)
	for url in reg:
		name = url.split('dn=')[-1].split('tr=')[0]
		name = urllib.unquote_plus(name)
		name= clean_name(name)
		addDir(name,'magnet:'+url,99,iconimage)	'''
###################################################################################
'''
									BLUDV 	FIM
'''
###################################################################################	
###################################################################################################################################################################################################
###################################################################################
'''
									THEPIRATEFILMESHD 	INICIO
'''
###################################################################################


def thepiratefilmeshd_pegar_pesquisa():
    keyb = xbmc.Keyboard('', 'Faca sua Busca...')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
        url = 'http://www.thepiratefilmeshd.com/?s='+parametro_pesquisa
        thepiratefilmeshd_pegar_videos(url)

		

def thepiratefilmeshd_pegar_categorias(url):#titled
	link = abrir_url(url).replace('\n','').replace('\r','')
	itemss = ['Home','Tutorias','Termos de Uso','DMCA']
	reg = re.compile('<li id="menu.*?" class="menu-.*?"><a href="(.*?)">(.*?)</a></li>').findall(link)
	for url,name in reg:
		if not name in itemss:
			addDir(name,url,2,iconimage)		
		

	
		
def thepiratefilmeshd_pegar_videos(url):#titled
	link = abrir_url(url).replace('\n','').replace('\r','')
	reg = re.compile('<h2 class="post-box-title">\s*<a href="(.*?)">(.*?)</a></h2><p class="post-meta">.*?<img.*?src="(.*?)" alt=').findall(link)
	for url,name,img in reg:
		name = name.split(' Torrent ')[0]#3
		addDir(name,url,999,img)		

	reg = re.compile('<span class="current">(.*?)</span><a href="(.*?)" class="page" title=".*?">.*?</a>').findall(link)
	for essa,proxima_pagina in reg:
		pro = int(essa)+1
		addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),proxima_pagina,2,PROXIMA_PAGINAS)	
		
	reg = re.compile("<span class='current'>(.*?)</span><a href='(.*?)' class='inactive'.*?>.*?</a>").findall(link)
	for essa,proxima_pagina in reg:
		pro = int(essa)+1
		addDir('PÁGINA ATUAL:  '+essa+'  /  PRÓXIMA PAGINA:  '+str(pro),proxima_pagina,2,PROXIMA_PAGINAS)	

	

		
def thepiratefilmeshd_pegar_links(url):#titled  (magnet.*?)
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	for url in reg:
		name = url.split('dn=')[-1].split('tr=')[0]
		name = urllib.unquote_plus(name)
		name= clean_name(name)
		addDir(name,url,99,iconimage)		
'''	reg = re.compile('<p style="text-align:.*?<a href="magnet:(.*?)">.*?</a>').findall(link)
	for url in reg:
		name = url.split('dn=')[-1].split('tr=')[0]
		name = urllib.unquote_plus(name)
		name= clean_name(name)
		addDir(name,'magnet:'+url,99,iconimage)'''	
	

###################################################################################
'''
									THEPIRATEFILMESHD 	FIM
'''
###################################################################################
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

def capturar_magnet(url,name,iconimage):
	link = abrir_url(url).replace('\n','').replace('\r','')		
	reg = re.compile(r'magnet:\?[^\'"\s<>\[\]]+').findall(link)
	for url in set(reg):
		name = url.split('dn=')[-1].split('tr=')[0]
		name = urllib.unquote_plus(name)
		name= clean_name(name)
		addDir(name,url,99,iconimage)	
		
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(51)")	
	

#################################	
def player_Torrents(url,name,iconimage):# Quasar|Pulsar|Yatp|Torrenter|XbmcTorrent|Torrentin|Ace Stream (apk)|Rox Player
	try:
		if selfAddon.getSetting('player_torrent') == "Quasar":
			url = 'plugin://plugin.video.quasar/play?uri='	+	urllib.quote_plus(url)
		elif selfAddon.getSetting('player_torrent') == "Pulsar":
			url = 'plugin://plugin.video.pulsar/play?uri='	+	urllib.quote_plus(url)
		elif selfAddon.getSetting('player_torrent') == "Yatp":
			url = 'plugin://plugin.video.yatp/?action=play&torrent='	+	urllib.quote_plus(url)
		elif selfAddon.getSetting('player_torrent') == "Torrenter":
			url = 'plugin://plugin.video.torrenter/?action=playSTRM&url='	+	urllib.quote_plus(url)	+	'&not_download_only=True'
		elif selfAddon.getSetting('player_torrent') == "XbmcTorrent":
			url = 'plugin://plugin.video.xbmctorrent/play/'	+	urllib.quote_plus(url)
		elif selfAddon.getSetting('player_torrent') == "Torrentin":
			url = 'plugin://plugin.video.torrentin/?uri='+urllib.quote_plus(url)
		elif selfAddon.getSetting('player_torrent') == "Ace Stream (apk)":
			sistema = platform()
			dialog = xbmcgui.Dialog()   
			if sistema == 'android':
				xbmc.executebuiltin('XBMC.StartAndroidActivity("org.acestream.media","android.intent.action.VIEW","","'+url+'")')
			else:
				xbmc.log('###################################                  INICIANDO SISTEMA       '+sistema+'        ################################################################')
				dialog.ok(addon_base,  "FUNCIONA APENAS EM SISTEMAS ANDROID !!!".decode('unicode_escape'),'')
				sys.exit(0)		
		pl=xbmc.PlayList(1)
		pl.clear()
		listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
		xbmc.PlayList(1).add(url, listitem)
		xbmc.Player().play(pl)
		sys.exit(0)
	except: 
		sys.exit(0)
	
	
	
	
############################################################################################################
#                                           FUNÇOES FEITAS                                                 #
############################################################################################################		
def setViewMenu() :
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		
		opcao = selfAddon.getSetting('menuVisu')
		
		if   opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
		elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
		elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")
		
def setViewFilmes() :
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')

		opcao = selfAddon.getSetting('filmesVisu')

		if   opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
		elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
		elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")
		elif opcao == '3': xbmc.executebuiltin("Container.SetViewMode(501)")
		elif opcao == '4': xbmc.executebuiltin("Container.SetViewMode(508)")
		elif opcao == '5': xbmc.executebuiltin("Container.SetViewMode(504)")
		elif opcao == '6': xbmc.executebuiltin("Container.SetViewMode(503)")
		elif opcao == '7': xbmc.executebuiltin("Container.SetViewMode(515)")
		
		
def abrir_url(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except IOError:#     except urllib2.HTTPError, e:
		dialog.notification(addon_base,'Não foi possivel acessar o servidor.',icones)
		sys.exit(0)
	
def abrir_url9988797978(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link



def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels={ "title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
	

############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################
              
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

      
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)



###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################
#abrir_url('https://goo.gl/oKyPTl')


if mode==None or url==None or len(url)<1:
        CATEGORIES()
			
		
elif mode==1: menu_sites(name)
###################################################################################		THEPIRATEFILMESHD
elif mode==2: thepiratefilmeshd_pegar_videos(url)
elif mode==3: thepiratefilmeshd_pegar_links(url)
elif mode==4: thepiratefilmeshd_pegar_categorias(url)
elif mode==5: thepiratefilmeshd_pegar_pesquisa()
###################################################################################		BLUDV
elif mode==6: comandotorrents_pegar_videos(url)
elif mode==7: comandotorrents_pegar_links(url)
elif mode==8: comandotorrents_pegar_categorias(url)
elif mode==9: comandotorrents_pegar_ano(url)
elif mode==10: comandotorrents_pegar_pesquisa()
elif mode==11: comandotorrents_pegar_foramtos(url)
###################################################################################		4K17
elif mode==12: _4k17_pegar_videos(url)
elif mode==13: _4k17_pegar_links(url)
elif mode==14: _4k17_pegar_categorias(url)
elif mode==15: _4k17_pegar_Uploaders()
elif mode==16: _4k17_pegar_pesquisa()
##################################################################################		TEUTORRENT
elif mode==17: teutorrent_pegar_videos(url)
elif mode==18: teutorrent_pegar_links(url)
elif mode==19: teutorrent_pegar_categorias(url)
elif mode==20: teutorrent_pegar_pesquisa()
#################################################################################		SERIESFILMESTORRENT
elif mode==21: torrentoon_pegar_videos(url)
elif mode==22: torrentoon_pegar_links(url)
elif mode==23: torrentoon_pegar_pesquisa()
elif mode==24: torrentoon_pegar_categorias(url)
elif mode==25: torrentoon_pegar_categorias_desenhos(url)
elif mode==26: torrentoon_pegar_categorias_series(url)
#################################################################################		LAPUMIAFILMES
elif mode==27: lapumiafilmes_pegar_videos(url)
elif mode==28: lapumiafilmes_pegar_links(url)
elif mode==29: lapumiafilmes_pegar_categorias(url)
elif mode==30: lapumiafilmes_pegar_pesquisa()
elif mode==31: lapumiafilmes_pegar_videosss(url)



elif mode==999: capturar_magnet(url,name,iconimage)



#################################################################################		PLAYER_TORRENT
elif mode==99: 
	player_Torrents(url,name,iconimage)
	xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)


xbmcplugin.endOfDirectory(int(sys.argv[1]))





