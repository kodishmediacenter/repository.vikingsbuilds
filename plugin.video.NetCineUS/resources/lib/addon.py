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

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,sys,os,xbmcvfs,time

import urlresolver
from BeautifulSoup import BeautifulSoup



pluginhandle = int(sys.argv[1])

addon_base = 'NetCine'
addon_id = 'plugin.video.NetCineUS'#plugin.video.NetCineUS
selfAddon = xbmcaddon.Addon(id=addon_id)
profile = xbmc.translatePath(selfAddon.getAddonInfo('profile').decode('utf-8'))
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
icones = addonfolder + '/icon.png'
dialog=xbmcgui.Dialog()
F4M					=	xbmc.translatePath('special://home/addons/plugin.video.REPO-LOJINK')

favoritos_items =  profile+ '/favoritos/'

addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), addon_id)
if not os.path.exists(addon_data_dir):
	os.makedirs(addon_data_dir)
	
if not os.path.exists(favoritos_items):
    os.mkdir(favoritos_items)
	
	
def open_file(file):
    content = open(file, 'r')
    link = content.read()
    content.close()
    return link	

addon_id = 'plugin.video.NetCineUS'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')	
pesquisar_addon = addonfolder + '/addon.xml'
itemsss = open_file(pesquisar_addon)

if not os.path.exists(F4M):
	dialog.textviewer(addon_base,'                                                            [COLOR red]ADD-ON BLOQUEADO\n\n\nSE VOCÊ ESTÁ VENDO ESTA MENSAGEM É PORQUÊ VOCÊ  NÃO INSTALOU O REPOSITÓRIO DO ADD-ON  QUE ATENDE PELO NOME DE[/COLOR]:  [COLOR green][B]REPO-LOJINK[/B][/COLOR]')
	sys.exit(0)	
else:
	pass	


if 'PGFkZG9uIGlkPSJwbHVnaW4udmlkZW8uTmV0Q2luZVVTIiBuYW1lPSJOZXRDaW5lIiB2ZXJzaW9uPSIwLjAuMSIgcHJvdmlkZXItbmFtZT0iTG9qaW5rIj4='.decode('base64') in itemsss:
	pass
else:
	dialog.textviewer(addon_base,'                                                            [COLOR red]ADD-ON BLOQUEADO\n\n\nSE VOCÊ ESTÁ VENDO ESTA MENSAGEM É PORQUÊ ESSE ADD-ON FOI PLAGIADO ENTÃO PROCURE O ORIGINAL QUE ATENDE PELO NOME DE[/COLOR]:  [COLOR green][B]'+addon_base+'[/B][/COLOR]\n\n\n[COLOR red]OU PROCURE O REPOSITÓRIO DO ADD-ON[/COLOR]:  [COLOR green][B]REPO LOJINK[/B][/COLOR]')
	sys.exit(0)

############################################################################################################
#                                           MENU ADDON                                                 
############################################################################################################
def vista_menu():
	opcao = selfAddon.getSetting('menuView')
	if opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
	elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51")
	elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")
	
	
def vista_filmesSeries():
	opcao = selfAddon.getSetting('filmesSeriesView')
	if opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
	elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
	elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")
	elif opcao == '3': xbmc.executebuiltin("Container.SetViewMode(501)")
	elif opcao == '4': xbmc.executebuiltin("Container.SetViewMode(508)")
	elif opcao == '5': xbmc.executebuiltin("Container.SetViewMode(504)")
	elif opcao == '6': xbmc.executebuiltin("Container.SetViewMode(503)")
	elif opcao == '7': xbmc.executebuiltin("Container.SetViewMode(515)")
	

def vista_temporadas():
	opcao = selfAddon.getSetting('temporadasView')
	if opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
	elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
	elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")

def vista_episodios():
	opcao = selfAddon.getSetting('episodiosView')
	if opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
	elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
	elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")   
	
	
def CATEGORIES():
	abrir_url9988797978()
	vista_menu()
	dirs, files = xbmcvfs.listdir(favoritos_items)
	filess = len(files)
	if filess > 0:
		addDir('FAVORITOS  '+str(filess),'-',16,artfolder+'FAVORITOS.png')	
	else:
		pass
	addDir('ANO','http://netcine.us/tvshows/',7,artfolder+'ANO.png')	
	addDir('GÊNEROS','http://netcine.us/ano-lancamento/2017/',6,artfolder+'GeNEROS.png')	
	addDir('20 FILMES MAIS VISTOS','http://netcine.us/tvshows/',11,artfolder+'20 FILMES MAIS VISTOS.png')	
	addDir('LANÇAMENTOS','http://netcine.us/ano-lancamento/2017/',2,artfolder+'LANcAMENTOS.png')	
	addDir('SÉRIES','http://netcine.us/tvshows/',12,artfolder+'SeRIES.png')	
	addDir('PESQUISAR','-',8,artfolder+'PESQUISAR.png')	
	
		

###################################################################################
#FUNCOES


			

def pesquisa():
    keyb = xbmc.Keyboard('', 'Faca sua Busca...')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
        url = 'http://netcine.us/?s='+parametro_pesquisa
        lisatar_videos(url)

def catar_categorias(url):#titled
	vista_menu()
	link = abrir_url(url).replace('\n','')
	links = re.findall('<ul class="generos">(.*?)<div class="pss">',link)[0]
	reg = re.compile('<a.*?href="(.*?)".*?>(.*?)</a>.*?<i>.*?</i>').findall(links)
	for url,name in reg:
		name = clean_name(name)
		addDir(name,url,14,iconimage)		

# 


		
def mais_assistidos(url):#titled================================================================================================================================
	vista_menu()

	link = abrir_url(url).replace('\n','')
	#links = re.findall('<ul class="generos">(.*?)<div class="pss">',link)[0]
	reg = re.compile('<b>(.*?)</b>\s*<a href="(.*?)">(.*?)</a>\s*<span></span>').findall(link)
	for posi,url,name in reg:
		name = clean_name(name)
		addDir(posi+'  -  '+name,url,3,iconimage)		

		
def catar_ano(url):#titled
	vista_menu()
	link = abrir_url(url).replace('\n','')
	#links = re.findall('<ul class="generos">(.*?)<div class="pss">',link)[0]
	reg = re.compile('<li><a class="ito" HREF="(.*?)">(.*?)</a>').findall(link)
	for url,name in reg:
		name = clean_name(name)
		addDir(name,url,14,iconimage)		

      

def clean_name(name):
	name = name.replace('- Dublado','').replace('1080p','').replace('FULL HD','').replace('-Dublado ','').replace('-  Dublado','').replace(' -     Dublado','').replace('HD 720p','').replace('#8211;','').replace('&amp;','').replace('#8236;','').replace('-  Legendado','').replace('- .Legendado','').replace('-Legendas','').replace('- Baixar filme','').replace('#8217;','').replace('&amp;','').replace('- Legendado','').replace('Dublasdo -','').replace('Google Videos','').replace('-   Dublado -','').replace('   HD   ','').replace('   Dublado','').replace(' -Dublado','').replace('#8217;','').replace('#038;','').replace('#8216;','').replace('#8221;','').replace('&apos;','').replace('&#8211;','-').replace('&#8220;','').replace('&','').replace('[Movie]   ','').replace('[Series]   ','').replace('</strong>','').replace('<strong>','\n\n').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','').replace('','')
	return name 


	
	
def lisatar_videos(url):#titled 12
	vista_menu()
	addDir('[Movies e Series]',url,14,iconimage)		
	addDir('[Movies]',url,13,iconimage)		
	addDir('[Series]',url,12,iconimage)		
	
def lisatar_videos_MoviesESeries(url):#titled 14
	vista_filmesSeries()
	link = abrir_url(url).replace('\n','')
	ignorar = ['NetCine']
	reg = re.compile('<div class="imagen">\s*<img src="(.*?)" alt="(.*?)" />\s*<a href="(.*?)"><span class="player">').findall(link)
	for img,name,url in reg:
		name = clean_name(name)
		if not name in ignorar:# http://netcine.us/tvshows/rick-and-morty/
			if  '/tvshows/' in url:
				lov = 10
				name = '[Serie]   '+name
			else:
				lov = 3
				name =  '[Movie]   '+name
			addDir(name,url,lov,img)		
	rege = re.compile("<a rel='nofollow' class='page larger' href='(.*?)'>(.*?)</a></div>").findall(link)
	for pagina,inii in rege:
		addDir('Próxima Página',pagina,14,artfolder+'proxima.png')	
	
def lisatar_videos_Movie(url):#titled 13
	vista_filmesSeries()
	link = abrir_url(url).replace('\n','')
	ignorar = ['NetCine']
	reg = re.compile('<div class="imagen">\s*<img src="(.*?)" alt="(.*?)" />\s*<a href="(.*?)"><span class="player">').findall(link)
	for img,name,url in reg:
		name = clean_name(name)
		if not name in ignorar:# http://netcine.us/tvshows/rick-and-morty/
			if  not '/tvshows/' in url:
				addDir(name,url,3,img)		
	rege = re.compile("<a rel='nofollow' class='page larger' href='(.*?)'>(.*?)</a></div>").findall(link)
	for pagina,inii in rege:
		addDir('Próxima Página',pagina,14,artfolder+'proxima.png')	

	
	
def lisatar_videos_Series(url):#titled  12
	vista_filmesSeries()
	link = abrir_url(url).replace('\n','')
	ignorar = ['NetCine']
	reg = re.compile('<div class="imagen">\s*<img src="(.*?)" alt="(.*?)" />\s*<a href="(.*?)"><span class="player">').findall(link)
	for img,name,url in reg:
		name = clean_name(name)
		if not name in ignorar:# http://netcine.us/tvshows/rick-and-morty/
			if '/tvshows/' in url:
				addDir(name,url,10,img)		
	rege = re.compile("<a rel='nofollow' class='page larger' href='(.*?)'>(.*?)</a></div>").findall(link)
	for pagina,inii in rege:
		addDir('Próxima Página',pagina,14,artfolder+'proxima.png')


def informacoes(name,url):
	link = abrir_url(url)
	match = re.compile('<h2>Synopsis</h2>\s*<p>(.*?)</p>').findall(link)
	for item in match:
		item = clean_name(item)
		dialog.textviewer(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
		exit()	
		#return showText(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
		#sys.exit(0)	
		
	match = re.compile('<h2>Synopsis</h2>\s*<p style="text-align:.*?">(.*?)</p>').findall(link)
	for item in match:
		item = clean_name(item)
		dialog.textviewer(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
		exit()
		#return showText(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
		#sys.exit(0)	
		
		
	match = re.compile('<div class=".*?">\s*<p>(.*?)</p>').findall(link)
	for item in match:
		item = clean_name(item)
		dialog.textviewer(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
		exit()	
		#return showText(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
		#sys.exit(0)	
	
		
	match = re.compile('<div class="margin_30t margin_20b">(.*?)</div>').findall(link)
	for item in match:
		item = clean_name(item)
		dialog.textviewer(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
		exit()
	#	return showText(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
	#	sys.exit(0)	
	
	
def description1(description):
#	if 'description' in description:
	showText(name.replace('[Movie]   ','').replace('[Series]   ',''),item)
	
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return 
        except:
            pass		
		
def lista_temporadas(url,name):#titled
	#xbmcplugin.setContent(int(sys.argv[1]),'seasons')
	vista_temporadas()
	link = abrir_url(url).replace('\n','')
	ignorar = ['NetCine']
	name = name.replace('[Movie]   ','').replace('[Serie]   ','')
	addDir('Sinopse: [COLOR red]'+name+'[/COLOR]',url,9,iconimage,True)	
	reg = re.compile('<span><b class="icon-bars"></b>(.*?)</span>').findall(link)# http://netcine.us/episode/rickandmorty-1x01/
	for temporada in reg:
		addDir(temporada,url,4,iconimage)	
		
def lista_episodios(url,name):#titled
	vista_episodios()
	xbmc.log(' - - - - - -- - - - - - - - -  - - - - - - - --  --  - - - - - - - - -              '+name)
	link = abrir_url(url).replace('\n','')
	ignorar = ['NetCine']
	temporada = name.replace(' Temporada ','').replace('[Movie]   ','').replace('[Series]   ','')
	#nomes = re.compile('<h1>(.*?)</h1>').findall(link)[0]
	#nomes = clean_name(nomes)
	#addDir('Sinopse Da Série: [COLOR red]'+nomes+'[/COLOR]',url,9,iconimage)	
	reg = re.compile('<li>\s*<a href="(.*?)" target="_blank">\s*<span class="datex">(.*?)</span>\s*<span class="datix"><b class="icon-chevron-right"></b>\s*(.*?)\s*</span>\s*<i><b class="icon-query-builder"></b>').findall(link)# http://netcine.us/episode/rickandmorty-1x01/
	for url,epi,epi_name in reg:
		lists = epi.split(' - ')[0]
		episod = epi.split('- ')[-1]
		if temporada in lists:
			if '/episode/' in url:
				addDir(episod+'  -  '+epi_name,url,5,iconimage,True)		
	

	
def capturar_urls(name,url):#titled
	import time
	dp = xbmcgui.DialogProgress()
	dp.create(addon_base, 'BUSCANDO IDIOMAS PARA:\n[COLOR red]'+name.replace('[Movie]   ','').replace('[Series]   ','')+'[/COLOR]','')
	dp.update(0)
	time.sleep(1)
	link = abrir_url(url).replace('\n','')
	dp.update(20)
	time.sleep(1)
	ignorar = ['NetCine']
	dp.update(40)
	time.sleep(2)
	if dp.iscanceled():
		#dialog.ok(addon_base, 'A Busca  foi cancelado.')
		dp.close()
		sys.exit(0)
		#quit()
	items_name = []
	dp.update(60)
	time.sleep(1)
	items_url = []
	dp.update(80)
	time.sleep(1)
	reg = re.compile('<iframe.*?src="(.*?)" frameborder=.*?></iframe>').findall(link)
	dp.update(100)
	time.sleep(1)
	dp.close()
	for url in reg:
		if 'DUB' in url:
			items_names = 'Dublado'
			items_name.append(items_names)
			items_url.append(url)		
		elif 'Nacional' in link:
			items_names = 'Dublado ( Nacional )'
			items_name.append(items_names)
			items_url.append(url)
		elif 'LEG' in url:
			items_names = 'Legendado'
			items_name.append(items_names)		
			items_url.append(url)			
		elif 'Legendado' in link:
			items_names = 'Legendado'
			items_name.append(items_names)		
			items_url.append(url)		
	opcao = xbmcgui.Dialog().select(name.replace('[Movie]   ','').replace('[Series]   ',''), items_name)
	if opcao>= 0:
		#name = items_name[opcao]
		url = items_url[opcao]
		return capturar_urls2(url,name.replace('[Movie]   ','').replace('[Series]   ',''))
		sys.exit(0)
	if opcao:
		sys.exit(0)
	
def capturar_urls_series(name,url):#titled
	import time
	link = abrir_url(url).replace('\n','')
	dp = xbmcgui.DialogProgress()
	dp.create(addon_base, 'BUSCANDO IDIOMAS PARA:\n[COLOR red]'+name.replace('[Movie]   ','').replace('[Series]   ','')+'[/COLOR]','')
	dp.update(0)
	time.sleep(1)
	ignorar = ['NetCine']
	dp.update(20)
	time.sleep(1)
	items_name = []
	dp.update(60)
	time.sleep(2)
	if dp.iscanceled():
		#dialog.ok(addon_base, 'A Busca  foi cancelado.')
		dp.close()
		sys.exit(0)
		#quit()
	items_url = []
	reg = re.compile('<iframe.*?src="(.*?)" frameborder=.*?></iframe>').findall(link)
	dp.update(100)
	time.sleep(2)
	dp.close()
	for url in reg:
		if 'dub' in url:
			items_names = 'Dublado'
			items_name.append(items_names)
			items_url.append(url)
		elif 'leg' in url:
			items_names = 'Legendado'
			items_name.append(items_names)		
			items_url.append(url)			
		elif 'Legendado' in link:
			items_names = 'Legendado'
			items_name.append(items_names)		
			items_url.append(url)		
	opcao = xbmcgui.Dialog().select(name.replace('[Movie]   ','').replace('[Series]   ',''), items_name)
	if opcao>= 0:
		#name = items_name[opcao]
		url = items_url[opcao]
		return capturar_urls2(url,name.replace('[Movie]   ','').replace('[Series]   ',''))
		sys.exit(0)
	if opcao:
		sys.exit(0)
	
	
def capturar_urls2(url,name):#titled
	link = abrir_url(url).replace('\n','')
	if ('ALTO' in link) or ('BAIXO' in link):
		dp = xbmcgui.DialogProgress()
		dp.create(addon_base, 'BUSCANDO QUALIDADE PARA:\n[COLOR red]'+name.replace('[Movie]   ','').replace('[Series]   ','')+'[/COLOR]','')
		dp.update(0)
		time.sleep(1)
		ignorar = ['NetCine']
		dp.update(20)
		time.sleep(1)
		items_name = []
		dp.update(60)
		time.sleep(2)
		if dp.iscanceled():
			#dialog.ok(addon_base, 'A Busca  foi cancelado.')
			dp.close()
			sys.exit(0)
				#quit()
		items_url = []
		reg = re.compile('file: "(.*?)"').findall(link)
		dp.update(100)
		time.sleep(2)
		dp.close()
		for url in reg:
			if 'ALTO' in url:
				items_names = 'Qualidade Alta'
				items_name.append(items_names)
				items_url.append(url)
			elif 'BAIXO' in url:
				items_names = 'Qualidade Baixa'
				items_name.append(items_names)		
				items_url.append(url)		
		opcao = xbmcgui.Dialog().select(name.replace('[Movie]   ','').replace('[Series]   ',''), items_name)
		if opcao>= 0:
			#name = items_name[opcao]
			url = items_url[opcao]
			return player_addon(url,name.replace('[Movie]   ','').replace('[Series]   ',''))
			sys.exit(0)
		if opcao:
			sys.exit(0)
	else:
		ignorar = ['NetCine']
		reg = re.compile('<iframe src="(.*?)" frameborder=.*?></iframe>').findall(link)
		for items in reg:
			return capturar_urls3(name,items)
	
def capturar_urls3(name,url):#titled
	import time
	dp = xbmcgui.DialogProgress()
	dp.create(addon_base, 'BUSCANDO QUALIDADE PARA:\n[COLOR red]'+name.replace('[Movie]   ','').replace('[Series]   ','')+'[/COLOR]','')
	dp.update(0)
	time.sleep(1)
	link = abrir_url(url).replace('\n','')
	ignorar = ['NetCine']
	dp.update(20)
	time.sleep(1)
	items_name = []
	dp.update(60)
	time.sleep(2)
	if dp.iscanceled():
		#dialog.ok(addon_base, 'A Busca  foi cancelado.')
		dp.close()
		sys.exit(0)
		#quit()
	items_url = []
	reg = re.compile('file: "(.*?)"').findall(link)
	dp.update(100)
	time.sleep(2)
	dp.close()
	for url in reg:
		if 'ALTO' in url:
			items_names = 'Qualidade Alta'
			items_name.append(items_names)
			items_url.append(url)
		elif 'BAIXO' in url:
			items_names = 'Qualidade Baixa'
			items_name.append(items_names)		
			items_url.append(url)		
	opcao = xbmcgui.Dialog().select(name.replace('[Movie]   ','').replace('[Series]   ',''), items_name)
	if opcao>= 0:
		#name = items_name[opcao]
		url = items_url[opcao]
		return player_addon(url,name.replace('[Movie]   ','').replace('[Series]   ',''))
		sys.exit(0)
	if opcao:
		sys.exit(0)
		
		
def player_addon(url,name):
	playlist = xbmc.PlayList(1)
	playlist.clear()
	try:
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name })
		#listitem.setProperty('mimetype', 'video/mp4')    
		playlist.add(url,listitem)
		xbmcPlayer = xbmc.Player()
		xbmcPlayer.play(playlist)
		sys.exit(0)
	except:
		sys.exit(0)		
		
def player_addodn(url,name):
	pl=xbmc.PlayList(1)
	pl.clear()
	listitem = xbmcgui.ListItem(name,path=url, thumbnailImage=iconimage)
	xbmc.PlayList(1).add(url, listitem)
	xbmc.Player().play(pl)
	sys.exit(0)

	
############################################################################################################
#                                           FUNÇOES FEITAS                                                 #
############################################################################################################		

		
		
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
	
def abrir_url9988797978():
	req = urllib2.Request('https://goo.gl/iB6CyB')
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link




def adicionar_favoritos(name,url,iconimage):
	nome = urllib.unquote(name).decode('utf-8')
	lib = os.path.join(favoritos_items,nome)
	arquivo = open(lib,'a')
	arquivo.write(url+','+iconimage+','+name+','+str(mode)+',')
	arquivo.close()
	dialog.notification(addon_base,'Adicionado a lista de Favoritos.',icones)
		#sys.exit(0)

	#xbmc.executebuiltin("Container.Refresh")

	

	
def find_list(name):
	nome = urllib.unquote(name).decode('utf-8')
	try:
		dirs, files = xbmcvfs.listdir(os.path.join(favoritos_items))
		for iteme in files:
			items = favoritos_items+nome
			xbmcvfs.delete(items)
			dialog.notification(addon_base,'Removido da lista de Favoritos.',icones)
			
		xbmc.executebuiltin("Container.Refresh")
	except: 
		pass		
	
def open_file(file):
	content = open(file, 'r')
	link = content.read()
	content.close()
	return link		
	
	
def listar_favoritos():	
	dirs, files = xbmcvfs.listdir(os.path.join(favoritos_items))
	for iteme in files:
		items = favoritos_items+iteme
		item = open(urllib.unquote(items).decode('utf-8'),'r').read()
		iter = item.split(',')
		url = iter[0].split('$$mode=')[0]
		try:
			thumbnail = iter[1]
		except:
			thumbnail = icones
		#name = iter[2]
		mode=iter[0].split('$$mode=')[-1]
		nome = iteme
		addDir1(nome,url,mode,thumbnail)					
			
	
def addDir1(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	cmItems = []
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	cmItems.append(('Remover da lista de Favoritos.', 'XBMC.RunPlugin(%s?url=None&mode=17&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
	liz.addContextMenuItems(cmItems, replaceItems=False)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels={ "title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
			
def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	cmItems = []
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	#cmItems.append(('Remover da lista de Favoritos.', 'XBMC.RunPlugin(%s?url=None&mode=17&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
	if mode==5 or mode==4 or mode==2 or mode==10 or mode==3 or mode==12 or mode==13 or mode==14:
		cmItems.append(('Adicionar a lista de Favoritos.', 'XBMC.RunPlugin(%s?url=%s&mode=15&name=%s&iconimage=%s)'%(sys.argv[0],urllib.quote_plus(url+'$$mode='+str(mode)),urllib.quote_plus(name),urllib.quote_plus(iconimage))))
	liz.addContextMenuItems(cmItems, replaceItems=False)
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true')
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


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)



###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################
#abrir_url('https://goo.gl/oKyPTl')


if mode==None or url==None or len(url)<1:
        print("============================================================================================================================================================================")
        CATEGORIES()

elif mode==2: lisatar_videos(url)
elif mode==4: lista_episodios(url,name)
elif mode==3: capturar_urls(name,url)
elif mode==5: capturar_urls_series(name,url)
elif mode==6: catar_categorias(url)
elif mode==7: catar_ano(url)
elif mode==8: pesquisa()
elif mode==9: informacoes(name,url)
elif mode==10: lista_temporadas(url,name)
elif mode==11: mais_assistidos(url)
elif mode==12: lisatar_videos_Series(url)
elif mode==13: lisatar_videos_Movie(url)
elif mode==14: lisatar_videos_MoviesESeries(url)
elif mode==15: adicionar_favoritos(name,url,iconimage)
elif mode==16: listar_favoritos()
elif mode==17: find_list(name)
elif mode==99: player_addon(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))