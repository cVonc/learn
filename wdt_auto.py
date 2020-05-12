# encoding=utf-8

import time
from selenium import webdriver

# 初始化
driver = webdriver.Chrome()
driver.get('http://dev.i.bim999.cn:9840/')
driver.maximize_window()


def login():
    # 登录
    username = driver.find_element_by_xpath('//*[@id="user"]')
    time.sleep(2)
    username.send_keys('admin')
    time.sleep(2)
    pwd = driver.find_element_by_xpath('//*[@id="pass"]')
    pwd.send_keys('Bim@999')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login-button"]').click()
    time.sleep(2)


def new_window():
    # 获取新窗口句柄
    driver.find_element_by_xpath(".//nb-action[5]/a/i").click()
    handles = driver.window_handles
    for handle in handles:
        if handle != driver.current_window_handle:
            time.sleep(2)
            driver.close()
            driver.switch_to.window(handle)


def select_element():
    # 选择目录
    driver.find_element_by_xpath(".//ul/p-treenode[1]/li/div/span[1]").click()
    time.sleep(2)  # 等待页面渲染
    driver.find_element_by_xpath(".//li/ul/p-treenode[2]/li/div/span[3]/span/a").click()
    time.sleep(2)


def upload_files():
    # 上传文件
    driver.find_element_by_xpath(".//div[2]/button[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//p-dropdown/div/div[3]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//div[4]/div/ul/li[3]").click()
    time.sleep(2)
    upload = driver.find_element_by_xpath(".//div[1]/span/input")
    time.sleep(2)
    upload.send_keys("F:\\company\\鹿山隧道施工进度计划.pdf")
    time.sleep(2)
    driver.find_element_by_xpath(".//div[1]/div[3]/p-footer/button[2]").click()
    time.sleep(2)


def delete_files():
    # 删除文件
    driver.find_element_by_xpath(".//th[1]/p-dtcheckbox/div").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//div[3]/div[1]/button[3]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//div[3]/button[1]").click()


def log_out():
    # 退出系统
    driver.find_element_by_xpath(".//app-root/div[1]/div/div[2]").click()
    time.sleep(2)  # 等待页面渲染
    driver.find_element_by_xpath(".//div[2]/p/span").click()
    time.sleep(2)
    driver.quit()


login()
new_window()
select_element()
upload_files()
delete_files()
log_out()
