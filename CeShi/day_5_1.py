from selenium import webdriver
import time
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
'''
1.用户登录
2.默认板块发帖
3.默认板块回帖
4.用户退出
'''

driver=webdriver.Chrome('../tools/chromedriver')   #打开窗口
driver.implicitly_wait(3)   #隐式等待
try:
    #1.登陆
    driver.get('http://127.0.0.1/upload/forum.php')
    driver.switch_to_window(driver.current_window_handle)

    adm=driver.find_element_by_id('ls_username')
    adm.send_keys('admin' + Keys.RETURN)
    pwd=driver.find_element_by_id('ls_password')
    pwd.send_keys('admin' + Keys.RETURN)
    print('登陆成功！')

    # 2.发帖
    #进入默认板块
    driver.switch_to_window(driver.current_window_handle)
    bk=driver.find_element_by_css_selector('.fl_icn')
    bk.click()
    print('进入默认板块')

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

    #3.回帖
    driver.switch_to_window(driver.current_window_handle)
    message_1=driver.find_element_by_name('message')
    message_1.send_keys('哈哈哈')
    sub=driver.find_element_by_id('fastpostsubmit')
    sub.click()
    print('回帖成功！')

    # Zhuye=driver.find_element_by_id('mn_forum')
    # Zhuye.click()

    #4.退出
    QUIT=driver.find_element_by_css_selector('.wp div p a:nth-child(18)')
    QUIT.click()
    print('退出成功！')
finally:
    time.sleep(3)
    print('关闭浏览器！')
    driver.quit()
