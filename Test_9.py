from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


browser = webdriver.Firefox(executable_path='./geckodriver')
browser.set_window_size(1980,1080)
browser.set_window_position(0,0)

sleep(2)
browser.get("http://chat.bekerina.com:3000/")
sleep(3)

browser.find_element_by_id("name-line").send_keys("vardas")
sleep(2)

submit_button = browser.find_element_by_xpath('//*[@id="send"]')
submit_button.click()

sleep(2)
browser.close()