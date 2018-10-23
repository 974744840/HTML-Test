from selenium.webdriver.common.by import By
from pageobject.base import BasePage

class Add_NewLuntanPage(BasePage):
    add_luntan_button=(By.CSS_SELECTOR,'.mainhd li:nth-child(7)')   #进入论坛按钮
    add_luntan_button_add=(By.CSS_SELECTOR,'.lastboard a')      #点击添加按钮.container form table tbody:nth-child(3) tr:nth-last-child(2) td:nth-child(3) input
    add_luntan_input_add_titelt=(By.CSS_SELECTOR,'.container form table tbody:nth-child(3) tr:nth-last-child(2) td:nth-child(3) input')
    #输入新模块名称
    add_luntan_button_up=(By.ID,'submit_editsubmit')    #提交


    def Add_new(self,iframe,content):
        self.click(*self.add_luntan_button)
        self.cut_iframe(iframe)
        self.click(*self.add_luntan_button_add)
        self.clear(*self.add_luntan_input_add_titelt)
        self.sendkeys(content,*self.add_luntan_input_add_titelt)
        self.click(*self.add_luntan_button_up)
        self.quit_iframe()


