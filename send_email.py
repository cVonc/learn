from selenium import webdriver
import unittest
import time


class VisitGoogleByChrome(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Chrome()

    def test_sendEmail(self):
        # 访问163邮箱的首页
        self.driver.get("https://mail.163.com/")
        # 打印当前网页的网址
        self.driver.maximize_window()
        # 点击密码登录
        self.pwd_link = self.driver.find_element_by_xpath("//a[text()='密码登录']")
        self.pwd_link.click()
        # 找到登录框的iframe
        login_input_iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")
        # 切换进登录框的iframe
        self.driver.switch_to.frame(login_input_iframe)

        self.user_name = self.driver.find_element_by_xpath("//input[@name='email']")
        self.pass_wd = self.driver.find_element_by_xpath("//input[@name = 'password']")
        self.login_button = self.driver.find_element_by_xpath("//a[@id ='dologin']")

        # 清空用户名
        self.user_name.clear()
        self.user_name.send_keys("17521346875")
        self.pass_wd.send_keys("Wen120208")
        self.login_button.click()
        time.sleep(5)

        # 点击“写信”button
        self.writer_button = self.driver.find_element_by_xpath("//span[text()='写 信']")
        self.writer_button.click()
        time.sleep(2)

        # 输入收件人的邮箱
        self.addressee = self.driver.find_element_by_xpath("//input[contains(@aria-label,'收件人地址输入框')]")
        self.addressee.send_keys('48458799@qq.com')

        # 输入邮件主题
        self.title = self.driver.find_element_by_xpath("//input[contains(@id,'subjectInput')]")
        self.title.send_keys('发给自己的一封邮件')

        # 上传文件
        self.uppload_file_link = self.driver.find_element_by_xpath("//input[@type = 'file']")
        # self.uppload_file_link = self.driver.find_element_by_xpath("//a[text()='添加附件']")
        self.uppload_file_link.send_keys(r"E:\ideaprojects\pycharm\2020-05-07 17_25_19_result.html")
        time.sleep(5)

        # 切换进入boby的iframe
        # boby_iframe = self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']")
        # self.driver.switch_to.frame(boby_iframe)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))

        # 输入邮件正文内容
        self.body = self.driver.find_element_by_xpath("html/body")
        self.body.send_keys("实现写邮件，上传附件的功能自动化用了。。。。。。。。")
        self.driver.switch_to.default_content()

        # 点击“发送”按钮
        self.send_email = self.driver.find_element_by_xpath("//header//span[text()='发送']")
        self.send_email.click()

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
