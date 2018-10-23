from test.base_test import BaseTestCase
import time
from pageobject.luntan_login import LoginPage
from pageobject.luntan_seek import SeekPage
from pageobject.luntan_user_quit import QuitPage
'''
用户登录
进行帖子搜索
搜索haotest帖子
进入搜索的帖子
验证帖子标题和期望的一致
用户退出
'''
class luntan_3(BaseTestCase):
    def test_luntan_3(self):
        '''登陆'''
        long=LoginPage(self.driver)
        long.search('admin','admin')

        '''搜索'''
        seek=SeekPage(self.driver)
        seek.seek('我最帅！哈哈哈')

        '''退出'''
        user_quit=QuitPage(self.driver)
        user_quit.quit()

