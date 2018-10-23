'''
发表投票帖子
进行投票
取出投票各个选项的名称以及投票比例
取出投票的主题名称
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome('../tools/chromedriver')   #打开窗口
driver.implicitly_wait(3)   #隐式等待
driver.get('http://127.0.0.1/upload/forum.php')
driver.switch_to_window(driver.current_window_handle)

adm = driver.find_element_by_id('ls_username')
adm.send_keys('admin')
pwd = driver.find_element_by_id('ls_password')
pwd.send_keys('admin' + Keys.RETURN)
print('登陆成功！')
driver.get('http://127.0.0.1/upload/forum.php?mod=viewthread&tid=31')

time.sleep(3)
bk=driver.find_element_by_css_selector('.fl_tb tr:nth-last-child(2) td:nth-child(2) a')
bk.click()
print('进入新板块板块')

time.sleep(3)
fat=driver.find_element_by_id('newspecial')
fat.click()
print('点击发帖')

time.sleep(3)

dj_fat=driver.find_element_by_css_selector('#editorbox > ul li:nth-child(2) a')
dj_fat.click()
print('发起投票按钮')


tp_tit=driver.find_element_by_css_selector('#postbox > div.pbt.cl > div input')
tp_tit.send_keys('*******我最帅********')
print('输入题目')

tp_1=driver.find_element_by_css_selector('#pollm_c_1 > p:nth-child(1) > input')
tp_1.send_keys('是的！')
print('投票1')

tp_2=driver.find_element_by_css_selector('#pollm_c_1 > p:nth-child(2) > input')
tp_2.send_keys('没错')
print('投票2')

tp_3=driver.find_element_by_css_selector('#pollm_c_1 > p:nth-child(3) > input')
tp_3.send_keys('非常对')
print('投票3')

fq_tp=driver.find_element_by_css_selector('#postsubmit')
fq_tp.click()
print('发起投票按钮')

time.sleep(3)
qr_tp=driver.find_element_by_css_selector('#option_3')
qr_tp.click()
print('投票选中')

qr_tp_button=driver.find_element_by_css_selector('#pollsubmit')
qr_tp_button.click()
print('投票按钮')



'''投票信息'''
tp_con_1=driver.find_element_by_css_selector('#poll > div.pcht > table > tbody > tr:nth-child(1) > td.pvt > label')
tp_con_1_1=driver.find_element_by_css_selector('#poll > div.pcht > table > tbody > tr:nth-child(2) > td:nth-child(2)')
print(tp_con_1.get_attribute('textContent'),tp_con_1_1.get_attribute('textContent'))


tp_con_2=driver.find_element_by_css_selector('#poll > div.pcht > table > tbody > tr:nth-child(3) > td.pvt > label')
tp_con_2_1=driver.find_element_by_css_selector('#poll > div.pcht > table > tbody > tr:nth-child(4) > td:nth-child(2)')
print(tp_con_2.get_attribute('textContent'),tp_con_2_1.get_attribute('textContent'))

tp_con_3=driver.find_element_by_css_selector('#poll > div.pcht > table > tbody > tr:nth-child(5) > td.pvt > label')
tp_con_3_1=driver.find_element_by_css_selector('#poll > div.pcht > table > tbody > tr:nth-child(6) > td:nth-child(2)')
print(tp_con_3.get_attribute('textContent'),tp_con_3_1.get_attribute('textContent'))

print(driver.title)