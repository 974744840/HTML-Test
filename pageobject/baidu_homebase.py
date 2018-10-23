from pageobject.base import BasePage
from selenium.webdriver.common.by import By

#继承BasePage,核心：把每一个页面定义为一个类，把所有相关的操作方法定义到基类里bases，而页面类的内容是该页面独有的方法和属性
# 一个*传的元组，两个*传的是字典，都是可变长度参数
class HomeBase(BasePage):

    '''这里是通过方法：find_element()查找定位'''
    '''定位方法：(By.属性,'属性值') '''
    '''定位了什么？定位了浏览器的输入框和按钮'''
    homebase_input_search_loc=(By.ID,'kw')
    homebase_button_search_loc=(By.ID,'su')

    def search(self,content):
        self.sendkeys(content,*self.homebase_input_search_loc)
        self.click(*self.homebase_button_search_loc)

