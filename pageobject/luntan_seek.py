from pageobject.base import BasePage
from selenium.webdriver.common.by import By
import time
from selenium .webdriver.common.keys import Keys

'''搜索帖子并验证'''
class SeekPage(BasePage):
    # see=(By.XPATH,'//*[@id="scbar_txt"]')
    seek_button=(By.CSS_SELECTOR,'#scbar_form > table > tbody > tr > td.scbar_btn_td')     #点击搜索按钮
    seek_coutent=(By.ID,'scform_srchtxt')       #输入内容的框
    seek_coutent_button=(By.CSS_SELECTOR,'#scform_form > tbody > tr > td.td_srchbtn')  #搜索按钮
    seek_alr_essay=(By.CSS_SELECTOR,'.pbw h3 a:nth-child(1)')  #搜索到的文章

    def seek(self,coutent):
        # self.sendkeys(coutent,*self.see)
        self.click(*self.seek_button)
        time.sleep(3)
        self.activate_window_cut_1()
        self.sendkeys(coutent,*self.seek_coutent)
        time.sleep(3)
        self.click(*self.seek_coutent_button)
        time.sleep(3)
        self.click(*self.seek_alr_essay)
        self.activate_window_cut_2()
        self.assert_title(coutent)


