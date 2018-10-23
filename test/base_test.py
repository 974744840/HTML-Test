from selenium import webdriver
import unittest
from framework.browser import BrowserEngine

'''这里的driver是Chrome浏览的对象'''
class BaseTestCase(unittest.TestCase):
    '''前提准备工作'''
    def setUp(self):
        browser=BrowserEngine()
        '''封装了整个浏览器配置的类对象'''
        self.driver=browser.open_browser()
        # self.driver=webdriver.Chrome('../tools/chromedriver.exe')
        # self.driver.implicitly_wait(3)

    def tearDown(self):
        '''测试结束操作：关闭浏览器'''
        self.driver.quit()


