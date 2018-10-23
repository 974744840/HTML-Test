from selenium.webdriver.common.by import By
from pageobject.base import BasePage


'''默认板块发布文章类'''

class ReleasePage(BasePage):

    '''查找元素'''
    MoRenBankuai_button=(By.CSS_SELECTOR,'.fl_tb tr:nth-last-child(2) td:nth-child(2) a')
    Art_Tiele_input_content=(By.NAME,'subject')
    Art_message_input_content=(By.NAME,'message')
    release_button=(By.XPATH,'//*[@id="fastpostsubmit"]')

    def Release(self,title,message):
        self.click(*self.MoRenBankuai_button)
        self.sendkeys(title,*self.Art_Tiele_input_content)
        self.sendkeys(message,*self.Art_message_input_content)
        self.click(*self.release_button)


