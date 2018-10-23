'''
用户登录
进行帖子搜索
搜索haotest帖子
进入搜索的帖子
验证帖子标题和期望的一致
用户退出
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('../tools/chromedriver')   #打开窗口
driver.implicitly_wait(3)   #隐式等待
driver.get('http://127.0.0.1/upload/forum.php')
driver.switch_to_window(driver.current_window_handle)

adm = driver.find_element_by_id('ls_username')
adm.send_keys('admin1')
pwd = driver.find_element_by_id('ls_password')
pwd.send_keys('admin1' + Keys.RETURN)
print('登陆成功！')


sousuo_button=driver.find_element_by_id('scbar_btn')
sousuo_button.click()
driver.switch_to_window(driver.window_handles[1])
print('进入搜索页并激活窗口')

shousuo=driver.find_element_by_id('scform_srchtxt')
shousuo.send_keys('text 111111')
print('输入查找内容')

cld=driver.find_element_by_id('scform_submit')
cld.click()
print('搜索按钮')
time.sleep(4)

jinru=driver.find_element_by_xpath('//*[@id="27"]/h3/a')
jinru.click()
print('进入搜索到的文章。')
driver.switch_to_window(driver.window_handles[2])

assert "text 111111" in driver.title

QUIT=driver.find_element_by_css_selector('#hd > div > div.hdc.cl div p a:nth-child(12)')
QUIT.click()
print('普通用户退出成功！')


