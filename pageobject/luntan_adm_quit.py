from pageobject.base import BasePage
from selenium.webdriver.common.by import By

class AdmQuitPage(BasePage):
    adm_quit=(By.CSS_SELECTOR,'.uinfo p:nth-child(1) a')

    def Adm_quit(self):
        self.click(*self.adm_quit)