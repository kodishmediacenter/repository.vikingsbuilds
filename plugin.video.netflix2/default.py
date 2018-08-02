import xbmcgui
import webbrowser
import xbmc

def browser_player(os,link):

    if os =='android':
        links = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+link+'' ) )
    else:
        links = webbrowser . open ( ''+link+'' )



if xbmc . getCondVisibility ('system.platform.android'):
    os = 'android'

else:
    os = 'null'

#browser_player(os,links)


dialog = xbmcgui.Dialog()
ret = dialog.select('[COLOR red][B]Kodish [/B][COLOR white][B]Netflix Laucher[/B][/COLOR]', ['Efetuar o Login', '','Series de A a Z', 'Filmes de A a Z','Originais Netflix','Novidades','Favoritos','Codigo Secreto da Netflix','Modo Kids'])

if ret ==0:
    links = "https://www.netflix.com/br/login"
    browser_player(os,links)

if ret ==2:
    links = "https://www.netflix.com/browse/genre/83?so=az"
    browser_player(os,links)

if ret ==3:
    links = "https://www.netflix.com/browse/genre/34399?so=az"
    browser_player(os,links)

if ret ==4:
    links = "https://www.netflix.com/browse/genre/839338?so=az"
    browser_player(os,links)

if ret ==5:
    links = "https://www.netflix.com/browse/genre/1592210"
    browser_player(os,links)

if ret ==6:
    links = "https://www.netflix.com/browse/my-list"
    browser_player(os,links)


if ret ==7:
    mexus = xbmc.Keyboard('', 'Digite codigo secreto da netflix:')
    mexus.doModal()
    chavemexus = mexus.getText()
    links = "https://www.netflix.com/browse/genre/"+chavemexus+""
    browser_player(os,links)

if ret ==8:
    links = "https://www.netflix.com/Kids"
    browser_player(os,links)

