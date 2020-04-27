import unittest

class TestChat(unittest.TestCase):

    def test_send_message(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas")
        sleep(2)

        browser.find_element_by_id("message").send_keys("labas")
        sleep(2)

        submit_button = browser.find_element_by_xpath('//*[@id="send"]')
        submit_button.click()

        self.assertIsNone(submit_button.click())

        sleep(3)
        browser.close()

    def test_enter_name(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas")
        sleep(2)

        submit_button = browser.find_element_by_xpath('//*[@id="send"]')
        submit_button.click()

        self.assertNotIn("vardas", "name-line")

        sleep(2)
        browser.close()

    def test_resize(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)
        browser.get("http://chat.bekerina.com:3000/")

        sleep(3)

        browser.set_window_position(500, 10)
        self.assertTrue(browser.set_window_position, (500, 10))

        browser.set_window_size(750, 808)
        self.assertTrue(browser.set_window_position, (750, 808))

        sleep(3)
        browser.close()

    def test_min_max(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)
        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(4)

        browser.minimize_window()
        sleep(2)


        browser.maximize_window()
        sleep(2)

        self.assertEquals(browser.minimize_window(), browser.maximize_window())

        sleep(3)
        browser.close()

    def test_keys(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("send").send_keys(Keys.ENTER)
        sleep(2)

        self.assertNotEqual(browser.find_element_by_id("send").send_keys(Keys.ENTER), "")

        browser.close()

    def test_scroll(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

        self.assertEqual(browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);"),
                         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);"))

        sleep(3)
        browser.close()

    def test_refresh(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        sleep(2)
        browser.refresh()

        self.assertNotEqual("vardas", "")

        sleep(2)
        browser.close()

    def test_send_message2(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Firefox(executable_path='./geckodriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas")
        sleep(2)

        browser.find_element_by_id("message").send_keys("labas")
        sleep(2)

        submit_button = browser.find_element_by_xpath('//*[@id="send"]')
        submit_button.click()

        self.assertIsNone(submit_button.click())

        sleep(6)
        browser.close()

    def test_enter_name2(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Firefox(executable_path='./geckodriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)
        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas")
        sleep(2)

        submit_button = browser.find_element_by_xpath('//*[@id="send"]')
        submit_button.click()

        self.assertNotIn("vardas", "name-line")

        sleep(2)
        browser.close()

    def test_resize2(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Firefox(executable_path='./geckodriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)
        browser.get("http://chat.bekerina.com:3000/")

        sleep(3)

        browser.set_window_position(500, 10)
        self.assertTrue(browser.set_window_position, (500, 10))
        browser.set_window_size(750, 808)
        self.assertTrue(browser.set_window_position, (750, 808))

        sleep(3)
        browser.close()

    def test_min_max2(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Firefox(executable_path='./geckodriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(4)

        browser.minimize_window()
        sleep(4)

        browser.maximize_window()
        sleep(4)

        self.assertEquals(browser.minimize_window(), browser.maximize_window())

        browser.close()

    def test_keys2(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Firefox(executable_path='./geckodriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas").send_keys(Keys.ENTER)
        sleep(2)

        self.assertNotEqual(browser.find_element_by_id("send").send_keys(Keys.ENTER), "")

        sleep(2)
        browser.close()

    def test_scroll2(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Firefox(executable_path='./geckodriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

        self.assertEqual(browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);"),
                         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);"))

        sleep(3)
        browser.close()

    def test_refresh2(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep

        browser = webdriver.Firefox(executable_path='./geckodriver')
        browser.set_window_size(1980, 1080)
        browser.set_window_position(0, 0)

        sleep(2)

        browser.get("http://chat.bekerina.com:3000/")
        sleep(3)

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        browser.find_element_by_id("name-line").send_keys("vardas")
        browser.find_element_by_id("message").send_keys("labas")

        sleep(2)
        browser.refresh()

        self.assertNotEqual("vardas", "")

        sleep(2)
        browser.close()

if __name__ == '__main__':
    unittest.main()
