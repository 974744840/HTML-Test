from selenium.webdriver.common.by import By
from pageobject.base import BasePage

'''进入默认板块删除类'''
class DeletePage(BasePage):
    MoRenBankuai_button = (By.CSS_SELECTOR, '.fl_tb tr:nth-last-child(2) td:nth-child(2) a')    #进入板块
    Check_input_button_1=(By.CSS_SELECTOR,'#threadlisttableid tbody:nth-child(2)  td:nth-child(2)') #删除复选框
    Check_input_button_2=(By.CSS_SELECTOR,'.bm_c div#mdly p a:nth-child(1)')    #删除按钮
    Check_input_button_3=(By.ID,'modsubmit')    #确认删除按钮
    Check_input_button_4=(By.ID,'mn_forum') #   返回主页

    def Delete(self):
        self.click(*self.MoRenBankuai_button)
        self.click(*self.Check_input_button_1)
        self.click(*self.Check_input_button_2)
        self.click(*self.Check_input_button_3)
        self.click(*self.Check_input_button_4)