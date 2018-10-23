#显示等待案例
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://baidu.com")
try:
    element = WebDriverWait(driver, 5).until(
    ec.element_to_be_clickable((By.CSS_SELECTOR, '.mnav'))
    )
    element.click()
    print('当前页面是：', driver.title)
finally:
    time.sleep(5)
    driver.quit()