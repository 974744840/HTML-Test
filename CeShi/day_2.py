from selenium import webdriver
import re
#1.
driver = webdriver.Chrome("./chromedriver.exe")
# try:
#     driver.get('http://www.baidu.com')
#     driver.switch_to_window(driver.current_window_handle)
#     print('百度已经打开！',driver.title)

    # tags=driver.find_elements_by_tag_name('a')
    # for i in tags:
    #     print(i)
    # print('个数是：',len(tags))
    #
    # for link in tags:
    #     print(link.get_attribute('href'))
    #     print(link.get_attribute('text'))
    # driver.find_element_by_link_text('新闻').click()
    # link2=driver.find_elements_by_link_text('')
    # link3=driver.find_element_by_partial_link_text()
    # link4=driver.find_elements_by_partial_link_text()
# finally:
#     driver.quit()

#2.
# driver = webdriver.Chrome("./chromedriver.exe")
# try:
#     driver.get('http://home.baidu.com/home/index/contact_us')
#     driver.switch_to_window(driver.current_window_handle)
#     print('百度已经打开！',driver.title)
#
#     # ym = driver.page_source
#     # print(re.findall(r"([a-zA-Z0-9_.+-]+@baidu.com)",ym))
#
#     classs=driver.find_elements_by_class_name('mail-content-text')
#     for email in classs:
#         email.get_property('span')
#         print(email)
#
# finally:
#     driver.quit()

#3.Xpth
# driver.find_elements_by_xpath('//input[@]')

#4.CSS
css=driver.find_elements_by_css_selector('#kw')
