from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import traceback
#拉勾网爬虫
#目的：爬到网站上的职位信息,进入列表页后，逐一获取信息

driver=webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")
    #document.querySelector('.item_con_list li:first-child .p_top a')   找到具体的CSS
    window_list=driver.current_window_handle    #激活当前窗口（首页）并存储给window_List
    driver.switch_to_window(window_list)        #目的：为了关闭第二个窗口回到第一个窗口
    print('拉勾首页已经打开,网页标题题目：', driver.title)

    while True:
        jobs = driver.find_elements_by_css_selector('.item_con_list li')  # 找到CSS
        #通过遍历逐一找到并打开,整个过程浏览器软件上只有两个页面，一个是首页一个是打开的页面
        for job in jobs:
            jobs_link=job.find_element_by_css_selector('.p_top a span')
            jobs_link.click()
            driver.switch_to_window(driver.window_handles[1])   #切换激活到点击进去的页面
            print('点击切换网页成功！')

            #通过CSS获取信息
            jot_company=driver.find_element_by_css_selector('.company')
            jot_name = driver.find_element_by_css_selector('.name')
            jot_money = driver.find_element_by_css_selector('.salary')

            print('公司：',jot_company.text,
                  '职位：',jot_name.text,
                  '薪资范围：',jot_money.text)
            driver.close()
            driver.switch_to_window(window_list)    #回到第一个窗口

        #显式等待：等到可以单机下一页的时候，点击或者没有点击完再进行判断是否有下一页。
        next_page=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'.item_con_pager .pager_container > *:last-child')))
        next_page_class=next_page.get_attribute('class')
        if 'pager_netx_disabled' in next_page_class:
            break
        else:
            next_page.click()
            time.sleep(3)
            print('进入下一页')
finally:
    time.sleep(5)
    driver.quit()