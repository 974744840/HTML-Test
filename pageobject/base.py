from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os.path
from selenium import webdriver

'''添加全局对象logger'''
logger=Logger(logger='BasePage').getlog()
'''
解释：因为Logger类的init方法里有一个参数：logger，
    这里换成了BasePage，就相当于把Logger() 这个对象里的参数
    换为了BasePage，在调用了获取方法，最后赋给了新的对象logger
'''

#所有页面的基类，封装了要用的到公共方法
class BasePage(object):
    '''定义初始化参数：driver'''
    def __init__(self,driver):
        self.driver=driver

    '''浏览器后退操作'''
    def back(self):
        self.driver.back()
        logger.info('点击后退按钮！')

    '''浏览器前进操作'''
    def forward(self):
        self.driver.forward()
        logger.info('点击前进按钮！')

    '''浏览器打开URL操作'''
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开一个URL！')

    '''浏览器关闭操作'''
    def quit_browser(self):
        self.driver.quit()
        logger.info('关闭浏览器！')

    def close(self):
        try:
            self.driver.close()
            logger.info('结束并关闭浏览器！')
        except Exception as e:
            logger.error('关闭并结束失败%s' % e)

    '''查找'''
    def find_element(self,*loc):
        try:
            #visibility_of_element_located方法：预期条件展示
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info('找到元素：%s',loc)
            return self.driver.find_element(*loc)
        except:
            logger.error('%s页面中未找到%s元素' % (self,loc))

    def find_elements(self,*loc):
        try:
            #visibility_of_element_located方法：预期条件展示
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            # logger.info('找到元素：%s',loc)
            return self.driver.find_element(*loc)
        except:
            logger.error('%s页面中未找到%s元素' % (self,loc))

    '''截图方法'''
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('获取路径及文件名成功，如果报错将保存到：/screenshots/')
        except Exception as e:
            self.get_windows_img()
            logger.error('出现报错现象，已保存截图！%s',e)

    '''清除文本'''
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info('文本已经清除')
        except Exception as e:
            self.get_windows_img()
            logger.info('文本未清除，报错以截图：%s',e)

    '''输入的方法'''
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info('文本输入成功：%s',text)
        except Exception as e:
            self.get_windows_img()
            logger.error('文本输入失败：%s',e)

    '''点击元素'''
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info('点击完成。')
            # if el.text==None:
            #     logger.info('点击完成！！')
            # else:
            #     logger.info('点击完成：%s', el.text)
        except Exception as e:
            logger.error('点击出错：%s',e)

    '''激活窗口'''
    def activate_window(self):
        try:
            self.driver.switch_to_window(self.driver.current_window_handle)
            logger.info('激活窗口成功。')
        except:
            logger.error('激活窗口失败。')

    '''切换窗口1'''
    def activate_window_cut_1(self):
        try:
            self.driver.switch_to_window(self.driver.window_handles[1])
            logger.info('切换窗口1成功。')
        except:
            logger.error('切换窗口1失败。')


    '''切换iframe'''
    def cut_iframe(self,loc):
        try:
            self.driver.switch_to.frame(loc)
            logger.info('切换iframe成功。')
        except:
            logger.error('切换iframe失败')

    '''退出iframe'''
    def quit_iframe(self):
        try:
            self.driver.switch_to.default_content()
            logger.info('退出iframe成功。')
        except:
            logger.error('退出iframe失败。')

    '''断言判断标题'''
    def assert_title(self,coutent):
        try:
            assert coutent in self.driver.title
            logger.info('标题一致。')
        except:
            logger.error('标题不一致')

    '''投票信息'''
    def vote_message(self,*loc):
        el=self.find_elements(*loc)
        try:
            mess=str(el.get_attribute('textContent'))
            logger.info(mess)
        except:
            logger.error('没有获取信息')

'''---------------补充方法------------未修改未引用'''
'''
主要就三个：
1.等待元素显示
2.等待页面加载完毕
3.判断未加载完毕超时
'''

# def until_display(self, by_type, by_value):
#     u"""等待一个元素显示，超时抛出异常，超时时间在configBase中设置"""
#     res = False
#     for i in range(1, config.element_display_wait, 1):
#         self.debug_info(constants.el_to_wait % (by_type, by_value, str(i)))
#
#         if self.is_display(by_type, by_value):
#             res = True
#             break
#         else:
#             self.isAlertPresent()
#             res = False
#
#     if not res:
#         raise NameError(constants.el_not_find % (
#             by_type, by_value, str(config.element_find_wait)))
#
#
# def is_page_load_complete(self):
#     u"""判断web页面是不是加载完毕"""
#     js = "return document.readyState"
#     result = self.driver.execute_script(js)
#     if result == "complete":
#         return True
#     else:
#         return False
#
#
# def until_page_load(self):
#     u"""等待一个页面加载完成，超时抛出异常，超时时间在configBase中设置"""
#     res = False
#     for i in range(1, config.element_find_wait, 1):
#         if self.is_page_load_complete():
#             res = True
#             break
#         else:
#             res = False
#         time.sleep(1)
#
#     if not res:
#         raise NameError(constants.Page_not_load % (
#             str(config.element_find_wait)))
