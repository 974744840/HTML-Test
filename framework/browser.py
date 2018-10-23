import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger='BrowserEngine').getlog()

'''
ConfigParser类是提供调用ini配置文件的类
主要用两个方法：read和get
'''
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+'/tools/chromedriver.exe'
    # ie_driver_path=dir+'/tools/....'
    # Firefox_driver_path=dir+'/tools/....'

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)  #读取路径里的内容

        '''配置浏览器'''
        browser=config.get('browserType','browserName')
        logger.info('你已经选择了浏览器：%s：',browser)

        '''配置URL'''
        url=config.get('testServer','URL')
        logger.info('要输入的URL是：%s',url)

        if browser=='Chrome':
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('找到Chrome的WebDriver。')
        elif browser=='Firefox':
            self.driver=webdriver.Firefox(self.chrome_driver_path)
            logger.info('找到了火狐浏览器的WebDriver。')
        elif browser=='IE':
            self.driver=webdriver.Ie(self.chrome_driver_path)
            logger.info('找到了IE浏览器的WebDriver。')

        self.driver.get(url)
        logger.info('成功打开URL：%s',url)

        self.driver.maximize_window()
        logger.info('窗口最大化。')
        self.driver.implicitly_wait(3)
        logger.info('等待3秒。')


        return self.driver


    def quit_browser(self):
        logger.info('关闭浏览器。')
        self.driver.quit()

