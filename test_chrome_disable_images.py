#!/usr/bin/env python
#encoding=utf-8
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
desired_caps = chrome_options.to_capabilities()
print desired_caps
print "+"*10
prefs = {}
#禁用图片
#prefs['profile.managed_default_content_settings.images'] = 2
#prefs['profile.default_content_settings.images'] = 2
#prefs['profile.default_content_settings'] = "{'images':2}"
#设置下载目录
#prefs['download.default_directory'] = '/home/mlzboy'
#chrome_options.add_experimental_option("prefs",prefs)
#chrome_options.binary_location = "/usr/bin/chromium-browser"
#prefs = {"profile.managed_default_content_settings.images":2}
prefs = {'profile.default_content_setting_values':{'images':2,'javascript':2}}
chrome_options.add_experimental_option("prefs",prefs)
#chrome_options.add_argument("disable-images")            
driver = webdriver.Chrome(executable_path="./chromedriver",chrome_options = chrome_options)
#driver = webdriver.Chrome(chrome_options = chrome_options)
#driver = webdriver.Chrome(chrome_options = chrome_options)
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.baidu.com")
print driver.page_source
print "======"




