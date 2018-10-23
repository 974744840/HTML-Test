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
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome('../tools/chromedriver')   #打开窗口
driver.implicitly_wait(3)   #隐式等待

driver.get('http://127.0.0.1/upload/forum.php')
driver.switch_to_window(driver.current_window_handle)

adm = driver.find_element_by_id('ls_username')
adm.send_keys('admin')
pwd = driver.find_element_by_id('ls_password')
pwd.send_keys('admin' + Keys.RETURN)
print('登陆成功！')


# bk = driver.find_element_by_css_selector('.fl_icn')
# bk.click()
# print('进入默认板块')
#
# delt=driver.find_element_by_css_selector('#threadlisttableid tbody:nth-child(2)  td:nth-child(2)')
# delt.click()
# dell=driver.find_element_by_css_selector('.bm_c div#mdly p a:nth-child(1)')
# dell.click()
# de1=driver.find_element_by_id('modsubmit')
# de1.click()
# print('删除成功！')

# Zhuye=driver.find_element_by_id('mn_forum')
# Zhuye.click()
# print('返回主页成功！')

guanli = driver.find_element_by_css_selector('.wp div p a:nth-child(16)')
guanli.click()
driver.switch_to_window(driver.window_handles[1])
print('进入管理中心！')

adm_pwd=driver.find_element_by_name('admin_password')
adm_pwd.send_keys('admin')
tijiao=driver.find_element_by_name('submit')
tijiao.click()
print('进入管理模块成功！')

gl_lt=driver.find_element_by_css_selector('.mainhd li:nth-child(7)')
gl_lt.click()
print('进入管理论坛')

driver.switch_to.frame("main")
tianjia_button=driver.find_element_by_css_selector('.lastboard a')
tianjia_button.click()
print('点击添加按钮')

tit=driver.find_element_by_css_selector('.container form table tbody:nth-child(3) tr:nth-last-child(2) td:nth-child(3) input')
# .container form table tbody:nth-child(3) td:nth-child(3) div input
tit.clear()
tit.send_keys('鑫鑫模块！')
print('模块名称')

tijiao=driver.find_element_by_id('submit_editsubmit')
tijiao.click()
driver.switch_to.default_content()#跳出iframe模块
print('模块提交')

time.sleep(4)
tuichu=driver.find_element_by_css_selector('.uinfo p:nth-child(1) a')
tuichu.click()
print('管理员退出成功')

QUIT = driver.find_element_by_css_selector('.wp div p a:nth-child(18)')
QUIT.click()
print('用户退出成功！')

adm=driver.find_element_by_id('ls_username')
adm.send_keys('admin1' + Keys.RETURN)
pwd=driver.find_element_by_id('ls_password')
pwd.send_keys('admin1' + Keys.RETURN)
print('登陆成功！')

# 2.发帖
#进入默认板块
driver.switch_to_window(driver.current_window_handle)
bk=driver.find_element_by_css_selector('.fl_tb tr:nth-last-child(2) td:nth-child(2) a')
bk.click()
print('进入新板块板块')

#输入帖子内容标题
ft=driver.find_element_by_name('subject')
ft.send_keys('text 111111')

#输入帖子内容
message=driver.find_element_by_name('message')
message.send_keys('11111111111')
print('标题和内容输入完毕！')
#发表
submit=driver.find_element_by_xpath('//*[@id="fastpostsubmit"]')
submit.click()
print('发布成功！')

message_1 = driver.find_element_by_name('message')
message_1.send_keys('哈哈哈')
sub = driver.find_element_by_id('fastpostsubmit')
sub.click()
print('回帖成功！')

QUIT=driver.find_element_by_css_selector('#hd > div > div.hdc.cl div p a:nth-child(12)')
QUIT.click()
print('普通用户退出成功！')