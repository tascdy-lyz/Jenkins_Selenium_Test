from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(3)


    def test_sleepWait(self):


        def wait(x):
            return  self.driver.find_element(By.XPATH,'//*[@id="kw"]').is_enabled()

        WebDriverWait(self.driver,10).until(wait)

        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('测试开发')

        sleep(5)

    def teardown(self):

        self.driver.quit()