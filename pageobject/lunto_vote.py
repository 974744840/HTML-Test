from pageobject.base import BasePage
from selenium.webdriver.common.by import By
import time

'''投票类'''
class VotePage(BasePage):
    release_button=(By.CSS_SELECTOR,'.fl_tb tr:nth-last-child(2) td:nth-child(2) a')        #进入板块
    go_new_button=(By.CSS_SELECTOR,'#newspecial')      #点击发帖
    go_new_vote=(By.CSS_SELECTOR,'#editorbox > ul li:nth-child(2) a')   #点击投票按钮
    vote_title=(By.CSS_SELECTOR,'#postbox > div.pbt.cl > div input')    #输入投票标题
    vote_chooes_1=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(1) > input')   #输入投票选项1
    vote_chooes_2=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(2) > input')    #输入投票选项2
    vote_chooes_3=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(3) > input')  # 输入投票选项3
    vote_chooes_button=(By.CSS_SELECTOR,'#postsubmit')      #点击发起投票
    chooes_vote=(By.CSS_SELECTOR,'#option_3')       #进行投票
    chooes_vote_button=(By.CSS_SELECTOR,'#pollsubmit')  #进行投票按钮确认

    vote_message_1 = (By.CSS_SELECTOR,'#poll > div.pcht > table > tbody > tr:nth-child(1) > td.pvt > label')
    vote_message_1_1 = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    vote_message_2 = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(3) > td.pvt > label')
    vote_message_2_1 = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(4) > td:nth-child(2)')
    vote_message_3 = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(5) > td.pvt > label')
    vote_message_3_1 = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(6) > td:nth-child(2)')

    def vote(self,title,cho_1,cho_2,cho_3):
        self.click(*self.release_button)
        time.sleep(3)
        self.click(*self.go_new_button)
        time.sleep(3)
        self.click(*self.go_new_vote)
        time.sleep(2)
        self.sendkeys(title,*self.vote_title)
        time.sleep(2)
        self.sendkeys(cho_1,*self.vote_chooes_1)
        time.sleep(2)
        self.sendkeys(cho_2, *self.vote_chooes_2)
        time.sleep(2)
        self.sendkeys(cho_3, *self.vote_chooes_3)
        time.sleep(2)
        self.click(*self.vote_chooes_button)
        time.sleep(2)
        self.click(*self.chooes_vote)
        time.sleep(2)
        self.click(*self.chooes_vote_button)
        time.sleep(2)
        self.vote_message(*self.vote_message_1)
        self.vote_message(*self.vote_message_1_1)
        self.vote_message(*self.vote_message_2)
        self.vote_message(*self.vote_message_2_1)
        self.vote_message(*self.vote_message_3)
        self.vote_message(*self.vote_message_3_1)