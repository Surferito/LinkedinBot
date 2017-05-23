# -*- coding: utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from .time_util import sleep

# Esta es la funcion principal. Hace click en los 10 perfiles y avanza hasta que llega a la url_fin
def click_perfiles(browser, url_inicio, url_fin):
	browser.get(url_inicio)
	sleep(8)

	#Hacemos un bucle que se ejecuta hasta llegar a url_fin
	bucle = True
	while bucle == True:
		
		url_actual = browser.current_url

		#compara la url actual con la fin para ver si para o sigue
		if url_actual != url_fin:
			ver_perfiles(browser, url_actual)
			siguiente_pagina(browser)
		else: 
			ver_perfiles(browser, url_actual)
			print("El programa ha llegado a su fin. Espero que haya merecido la pena!! ;)")
			bucle = False 

""" Esta funcion entra uno a uno en cada perfil, hay 10 por pagina. Entra, espera y vuelve atras. 
Al volver atras hace scroll dependiendo de la posicion """
def ver_perfiles(browser, url_actual):
	for x in range(0, 10):
		
		if x > -1 and x < 3:
			
			click_perfil(browser, x, 150)
			viendo_perfil(browser)
			browser.back()
			print("Vuelve a la pagina de resultados y espera 6 sg")
			sleep(6)
			url_correcta(browser, url_actual)

		elif x > 2 and x < 6:
			click_perfil(browser, x, 550)
			viendo_perfil(browser)
			browser.back()
			print("Vuelve a la pagina de resultados y espera 6 sg")
			sleep(6)
			url_correcta(browser, url_actual)

		elif x > 5 and x < 9:
			#Hacemos scroll progresivo
			scroll_pagina = browser.execute_script("scroll(0, 550);")
			print("Hace scroll")
			sleep(2)
			click_perfil(browser, x, 1050)
			viendo_perfil(browser)
			browser.back()
			print("Vuelve a la pagina de resultados y espera 6 sg")
			sleep(6)
			url_correcta(browser, url_actual)

		elif x == 9:
			#Hacemos scroll progresivo
			scroll_pagina = browser.execute_script("scroll(0, 500);")
			sleep(2)
			scroll_pagina = browser.execute_script("scroll(0, 1200);")
			sleep(1)
			scroll_pagina = browser.execute_script("scroll(0, 1600);")
			print("Hace scroll")
			sleep(6)
			click_perfil(browser, x, 1800)
			viendo_perfil(browser)
			browser.back()
			print("Vuelve a la pagina de resultados y espera 6 sg")
			sleep(6)
			url_correcta(browser, url_actual)

""" ------------------------ Funciones ----------------------------- """

""" Funcion para comprobar url al volver del perfil. 
Deberia ser igual a la que tenia antes de entrar al perfil. """ 
def url_correcta(browser, url_actual):
	url = browser.current_url
	if url_actual != url:
		print("Linkedin fallo... redirigiendo a donde estabamos")
		browser.get(url_actual)
		sleep(6)

""" Funcion que hace scroll indicado, luego hace click en el perfil 
y espera 6 segundos """
def click_perfil(browser, x, pixels):
	scroll_pagina = browser.execute_script("scroll(0, %d);" % pixels)
	print("Hace scroll")
	sleep(10)
	elementos = browser.find_elements_by_xpath('//*[@class="name-and-icon"]')
	sleep(4)
	print("Total de elementos encontrados: " + str(len(elementos)))
	sleep(3)
	print("Posicion: " + str(x) + " - Nombre: " + elementos[x].text)
	ActionChains(browser).move_to_element(elementos[x]).click().perform()
	sleep(6)
	print("Hace click en el perfil: " + str(x))

""" Funcion que hace scroll progresivo al entrar en el perfil """
def viendo_perfil(browser):
	sleep(1)
	scroll_pagina = browser.execute_script("scroll(0, 150);")
	sleep(3)
	scroll_pagina = browser.execute_script("scroll(0, 350);")
	sleep(4)
	scroll_pagina = browser.execute_script("scroll(0, 650);")
	sleep(3)
	print("Hace scroll en el perfil")
	scroll_pagina = browser.execute_script("scroll(0, 100);")
	sleep(4)

""" Esta hace scroll progresivo hasta el final y luego hace click en siguiente 
para ver los proximos 10 perfiles """
def siguiente_pagina(browser): 
	scroll_pagina = browser.execute_script("scroll(0, 1000);")
	sleep(3)
	scroll_pagina = browser.execute_script("scroll(0, 1800);")
	print("Hace scroll hasta el final progresivo")
	sleep(3)
	siguiente = browser.find_element_by_xpath("//button[@class='next']")
	sleep(2)
	print("Hace click en next para pasar a la siguiente pagina")
	ActionChains(browser).move_to_element(siguiente).click().perform()
	sleep(10)



