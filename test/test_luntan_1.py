from test.base_test import BaseTestCase
import time
import unittest
from pageobject.luntan_login import LoginPage
from pageobject.luntan_release import ReleasePage
from pageobject.luntan_reply import ReplyPage
from pageobject.luntan_user_quit import QuitPage

class LunTan_1(BaseTestCase):

    def test_luntan_login(self):

        '''登陆操作'''
        loginpage=LoginPage(self.driver)
        loginpage.search('admin','admin')
        time.sleep(3)

        '''发布操作'''
        releasepage=ReleasePage(self.driver)
        time.sleep(3)
        releasepage.Release('哈哈哈——1','我最帅！！！！')

        '''回复操作'''
        reply=ReplyPage(self.driver)
        time.sleep(3)
        reply.reply('嘻嘻，你说的很对！！！')

        '''用户退出'''
        quit=QuitPage(self.driver)
        time.sleep(3)
        quit.quit()


if __name__=='main':
    unittest.main()
