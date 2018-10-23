from pageobject.base import BasePage
from selenium.webdriver.common.by import By

class QuitPage(BasePage):

    user_quit_button=(By.CSS_SELECTOR,'.wp div p a:nth-child(18)')

    def quit(self):
        self.click(*self.user_quit_button)