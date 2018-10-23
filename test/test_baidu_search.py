from test.base_test import BaseTestCase
from pageobject.baidu_homebase import HomeBase
import time
import unittest

class BaiduSearch(BaseTestCase):

    def test_baidu_search(self):
       home_page=HomeBase(self.driver)
       time.sleep(3)
       home_page.search('python')
       time.sleep(3)

if __name__=='__main':
   unittest.main()

