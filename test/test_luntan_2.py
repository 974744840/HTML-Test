from test.base_test import BaseTestCase
import time
import unittest
from pageobject.luntan_login import LoginPage
from pageobject.luntan_delete import DeletePage
from pageobject.luntan_go_adm import GoAdmPage
from pageobject.luntan_add_new import Add_NewLuntanPage
from pageobject.luntan_adm_quit import AdmQuitPage
from pageobject.luntan_user_quit import QuitPage
from pageobject.luntan_release import ReleasePage
from pageobject.luntan_reply import ReplyPage

'''
管理员用户登录
进入默认板块，删除帖子
进入版块管理(管理中心--论坛)
创建新的版块
管理员退出
普通用户登录
在新的版块下发帖
回复帖子
'''
class LunTan_2(BaseTestCase):
    def test_lun_2(self):
        '''管理员登陆'''
        adm_long=LoginPage(self.driver)
        adm_long.search('admin','admin')
        time.sleep(2)

        '''删除帖子'''
        delete=DeletePage(self.driver)
        delete.Delete()
        time.sleep(2)

        '''进入管理中心'''
        go_adm=GoAdmPage(self.driver)
        go_adm.Go_adm('admin')
        time.sleep(2)

        '''添加新模块'''
        add_new=Add_NewLuntanPage(self.driver)
        add_new.Add_new('main','我的最帅模块！')
        time.sleep(2)

        '''管理员管理中心退出'''
        adm_quit=AdmQuitPage(self.driver)
        adm_quit.Adm_quit()
        time.sleep(2)

        '''管理员用户退出'''
        userquit = QuitPage(self.driver)
        userquit.quit()
        time.sleep(2)

        '''普通用户登陆'''
        user_long=LoginPage(self.driver)
        user_long.search('admin1','admin1')
        time.sleep(2)

        '''普通用户在新帖下发帖并回复'''
        release=ReleasePage(self.driver)
        release.Release('我最帅！哈哈哈','是的！你说的没错。')
        time.sleep(2)
        reply=ReplyPage(self.driver)
        time.sleep(3)
        reply.reply('嘻嘻，你说的很对！！！')


        '''普通用户退出'''
        userquit=QuitPage(self.driver)
        userquit.quit()
        time.sleep(2)