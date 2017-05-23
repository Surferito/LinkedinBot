""" Modulo utilizado para el login """
from .time_util import sleep
from selenium.webdriver.common.action_chains import ActionChains

"""Funcion para logear al usuario en linkedin"""
def login_user(browser, username, password):

  browser.get('https://www.linkedin.com/')

  #Busca el elemento input e introduce usuario, contrasena
  inputs = browser.find_elements_by_xpath("//form/input")
  action = ActionChains(browser).move_to_element(inputs[0]).click().send_keys(username) \
          .move_to_element(inputs[1]).click().send_keys(password).perform() 

  #click en sign in
  sign_in = inputs[2]
  ActionChains(browser).move_to_element(sign_in).click().perform()   

  sleep(2)
  
  #Comprueba si el usuario esta logeado
  aside = browser.find_elements_by_xpath('//aside')
  
  if aside is not None:
    return True
  else:
    return False
  
  
