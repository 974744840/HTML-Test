#iframe执行嵌套

from selenium import webdriver
import time
from selenium .webdriver.common.keys import Keys

driver=webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(10)
try:
    driver.get('https://mail.163.com/')
    driver.switch_to_window(driver.current_window_handle)
    driver.switch_to.frame("x-URS-iframe")  #进入iframe
    elment=driver.find_element_by_name('email')
    elment.send_keys('hello')
finally:
    time.sleep(5)
    driver.quit()