from test.base_test import BaseTestCase
import time
from pageobject.luntan_login import LoginPage
from pageobject.lunto_vote import VotePage
'''
发表投票帖子
进行投票
取出投票各个选项的名称以及投票比例
取出投票的主题名称
'''
class Luntan_4(BaseTestCase):

    '''如果想执行两个方法两个业务需要加：@classmethod'''
    def test_luntan_4(self):
        long=LoginPage(self.driver)
        long.search('admin','admin')
        time.sleep(3)

        vote=VotePage(self.driver)
        vote.vote('****我最帅****','是的！','对滴','非常对')