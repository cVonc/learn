# coding=utf-8
'''
Created on 2017-6-14
@author: 冯文川
Project:通过测试套件执行多个测试用例，并生成报告
'''
import HTMLTestRunner
import unittest
import os
import time

listaa = "E:\\ideaprojects\\pycharm"


def createsuite1():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='auto_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
filename = "E:\\ideaprojects\\pycharm\\" + now + "_result.html"
fp = open(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'富阳大盘山项目登录验证功能测试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())

# 关闭文件流，不关的话生成的报告是空的
fp.close()
