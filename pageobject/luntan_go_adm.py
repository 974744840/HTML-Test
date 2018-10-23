from selenium.webdriver.common.by import By
from pageobject.base import BasePage

class GoAdmPage(BasePage):

    adm_button=(By.CSS_SELECTOR,'.wp div p a:nth-child(16)')
    adm_input_pwd=(By.NAME,'admin_password')
    adm_input_button=(By.NAME,'submit')

    def Go_adm(self,coutent):
        self.click(*self.adm_button)
        self.activate_window_cut_1()
        self.sendkeys(coutent,*self.adm_input_pwd)
        self.click(*self.adm_input_button)