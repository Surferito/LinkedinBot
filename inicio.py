# -*- coding: utf-8 -*-

"""El objetivo de este bot es ver perfiles"""

from linkedinbot import LinkedinBot

#introduce la url por la quieres que el bot empiece a ver perfiles 
inicio = 'https://laurldeinicio.com'

#introduce la url donde quieres que pare 
fin = 'https://laurlfin.com/search&page=50'

# Objeto sesion
session = LinkedinBot(username='blablabla@email.com', password='contrasena', url_inicio=inicio, url_fin=fin)

#Ejecuta la función de login y luego la de hacer clicks
session.login()
session.hacer_clicks()


"""Esta funcion limpia cookies y cierra el browser"""
session.fin()

""" 
*** TO-DO *** 

1. Hacer una funcion que haga scroll progresivo. Le metemos pixels y va bajando hasta la cantidad introducida.
2. Introcudir funcion que espera que cargue el navegador con try execept
3. Meterle un contador que al acabar diga el total de perfiles vistos
4. Funcion que conecte si tenemos contactos en comun

"""