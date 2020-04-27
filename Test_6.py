from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


browser = webdriver.Chrome (executable_path='./chromedriver')
browser.set_window_size(1980,1080)
browser.set_window_position(0,0)

sleep(2)

browser.get("http://chat.bekerina.com:3000/")
sleep(3)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

sleep(3)
browser.close()
