from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


browser = webdriver.Chrome (executable_path='./chromedriver')
browser.set_window_size(1980,1080)
browser.set_window_position(0,0)

sleep(2)
browser.get("http://chat.bekerina.com:3000/")

sleep(3)

browser.set_window_position(500,10)
browser.set_window_size(750,808)


sleep(3)
browser.close()