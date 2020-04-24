# -*- coding: utf-8 -*-

import urllib2
from colorama import Back, Fore, init

init(autoreset=True)

def hunter():
    while True:
        print '''
#     #                                   
#     # #    # #    # ##### ###### #####  
#     # #    # ##   #   #   #      #    # 
####### #    # # #  #   #   #####  #    # 
#     # #    # #  # #   #   #      #####  
#     # #    # #   ##   #   #      #   # 
#     #  ####  #    #   #   ###### #    # 
Version: 1.2
Codigo escrito por: Angelo Mass - Darko.

El autor no se hace responsable por el uso que le den a la herramienta.

Ingrese el usuario que quiere rastrear.'''
        usuario = raw_input('Darko@Hunter$ ')
        formatear = 'https://www.instagram.com/' + usuario
        url = formatear
        try:
            hdr = {'User-Agent':'Mozilla/5.0'}
            req = urllib2.Request(url,headers=hdr)
            html = urllib2.urlopen(req).read()
            if html.find('<h2>Esta página no está disponible') == -1:
                print Fore.GREEN + '[*]El usuario "' + usuario + '" existe en Instagram. Consulte la siguiente url: ' + url
            else: 
                print Fore.RED +  '[*]El usuario "' + usuario + '" no existe en Instagram.'
        except:
            print Fore.YELLOW + '[*]Ha ocurrido un error al consultar si el usuario "' + usuario + '" existe en Instagram.'

        formatear = 'https://m.facebook.com/' + usuario
        url = formatear
        try:
            hdr = {'User-Agent':'Mozilla/5.0'}
            req = urllib2.Request(url,headers=hdr)
            html = urllib2.urlopen(req).read()
            if html.find('Es posible que el enlace que seleccionaste esté dañado o que se haya eliminado la página.') == -1:
                print Fore.GREEN + '[*]El usuario "' + usuario + '" existe en Facebook. Consulte la siguiente url: ' + url
            else:
                print Fore.RED +  '[*]El usuario "' + usuario + '" no existe en Facebook.'
        except:
            print Fore.YELLOW + '[*]Ha ocurrido un error al consultar si el usuario "' + usuario + '" existe en Facebook.'

        formatear = 'https://mobile.twitter.com/' + usuario
        url = formatear
        try:
            hdr = {'User-Agent':'Mozilla/5.0'}
            req = urllib2.Request(url,headers=hdr)
            html = urllib2.urlopen(req).read()
            if html.find('This account doesn’t exist') == -1:
                print Fore.GREEN + '[*]El usuario "' + usuario + '" existe en Twitter. Consulte la siguiente url: ' + url
            else:
                print Fore.RED +  '[*]El usuario "' + usuario + '" no existe en Twitter.'
        print Fore.YELLOW + '[*]Ha ocurrido un error al consultar si el usuario "' + usuario + '" existe en Twitter.'

hunter()

#Codigo escrito por Angelo Mass - Darko.

#La herramienta fue diseñada para el grupo
#"Auditoria global" y para la pagina
#"black hat"

#Hackea El Planeta.
