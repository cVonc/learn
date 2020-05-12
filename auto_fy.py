import time

from selenium import webdriver


class Fy(object):
    def __init__(self):
        self.driver = webdriver.Chrome()  # 创建Chrome对象.
        # 操作这个对象.
        self.driver.get('http://shby.bim999.net')  # 访问.
        time.sleep(2)

    def login(self):
        username = self.driver.find_element_by_xpath('//*[@id="user"]')
        username.send_keys('admin')
        time.sleep(2)
        pwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pwd.send_keys('Bim@999')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login-button"]').click()
        time.sleep(2)

    def __del__(self):
        self.driver.quit()


ter = Fy()
ter.login()
del ter
