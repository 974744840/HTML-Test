from pageobject.base import BasePage
from selenium.webdriver.common.by import By


'''登陆类'''
class LoginPage(BasePage):
    '''定位账号密码输入框'''
    luntan_input_user=(By.ID,'ls_username')
    luntan_input_pwd=(By.ID,'ls_password')
    luntan_input_button=(By.CSS_SELECTOR,'#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button')

    '''输入账号密码并点击按钮'''
    def search(self,user,pwd):
        self.sendkeys(user,*self.luntan_input_user)
        self.sendkeys(pwd,*self.luntan_input_pwd)
        self.click(*self.luntan_input_button)
        self.activate_window()

