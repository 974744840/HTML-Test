from pageobject.base import BasePage
from selenium.webdriver.common.by import By

'''回复帖子'''
class ReplyPage(BasePage):

    '''定位元素'''
    reply_input_coutent=(By.NAME,'message')
    reply_input_button=(By.NAME,'replysubmit')

    '''输入内容并点击'''
    def reply(self,coutent):
        self.sendkeys(coutent,*self.reply_input_coutent)
        self.click(*self.reply_input_button)