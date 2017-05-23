from datetime import datetime
from os import environ
from random import randint
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


from .login_util import login_user
from .ver_perfiles import click_perfiles
from .time_util import sleep


class LinkedinBot:
  """Class to be instantiated to use the script"""
  def __init__(self, username=None, password=None, url_inicio=None, url_fin=None):

    chrome_options = Options()
    chrome_options.add_argument('--dns-prefetch-disable')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--lang=en-US')
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
    self.browser = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=chrome_options)
    self.browser.implicitly_wait(25)

    self.username = username 
    self.password = password 
    self.url_inicio = url_inicio
    self.url_fin = url_fin

  """ Esta funcion logea al usuario """
  def login(self):
    if not login_user(self.browser, self.username, self.password):
      print('No te he podido logear!! :(')
      
    else:
      print('Estamos ya dentro de Linkedin!! ;)')

    return self
  """ Esta funcion llama a click_perfiles: hace click en los perfiles, los ve, vuelve y avanza """
  def hacer_clicks(self):

    click_perfiles(self.browser, self.url_inicio, self.url_fin)

    return self


  #Termina la sesion
  def fin(self):
    
    self.browser.delete_all_cookies()
    self.browser.close()

    print('')
    print('Terminado')
    print('-------------')
