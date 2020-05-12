import time

from selenium import webdriver


driver = webdriver.Chrome()     # 创建Chrome对象.
# 操作这个对象.
driver.get('http://www.yjjhc001.cn/')     # get方式访问百度.
time.sleep(2)

username = driver.find_element_by_xpath('//*[@id="user"]')
username.send_keys('shuian')
time.sleep(2)
pwd = driver.find_element_by_xpath('//*[@id="pass"]')
pwd.send_keys('123456')
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="login-button"]').click()
time.sleep(2)


user = driver.find_element_by_xpath('/html/body/ngx-app/ngx-pages/ngx-sample-layout/nb-layout/div[1]/div/nb-layout-header/nav/ngx-header/nb-actions/nb-action[1]/nb-user/div').click()
user_exit = driver.find_element_by_xpath('//*[@id="cdk-overlay-0"]/nb-context-menu/nb-menu/ul/li[3]/a/span').click()
time.sleep(2)
driver.quit()
