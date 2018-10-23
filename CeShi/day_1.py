from selenium import webdriver
from selenium .webdriver.common.keys import Keys
import time


# 1.实现简单的代码调用浏览器打开网站
#新建一个webdriver的对象：driver,并执行.exe文件
# driver = webdriver.Chrome("./chromedriver.exe")
#模拟HTTP中GET请求
# driver.get("http://www.python.org")
# assert 断言查找标题是否存在，判断是否登陆
# assert "Python" in driver.title

#2.打开网站找到元素输入并查找
# driver = webdriver.Chrome("./chromedriver.exe")
# driver.get("http://www.Yahoo.org")
# assert "Yahoo" in driver.title
# #查找一个元素名字为'p'的元素，赋给elem
# elem=driver.find_element_by_name('p')
# #调用函数输入
# elem.send_keys('hhhhhhhhhh'+ Keys.RETURN)
# driver.quit()

#3.打开百度进行搜索，并检查是否成功
driver = webdriver.Firefox("../tools/geckodriver.exe")
try:
    #显示等待5秒
    driver.implicitly_wait(5)
    driver.get("http://www.baidu.com")
    #激活当前窗口
    driver.switch_to.window(driver.current_window_handle)
    #输出获取到的标题名
    print('百度已经打开',driver.title)
    #查找输入框id赋值给serch_input
    serch_input=driver.find_element_by_id('kw')
    #提交搜索内容并提交
    serch_input.send_keys('python')
    serch_input.submit()
    #验证提交的内容，找到 “百度为您找到相关结果约100,000,000个” 的class元素的名字：nums
    nums=driver.find_element_by_class_name('nums_text')
    #控制台打印找到的内容
    print(nums.text)
    #再次激活窗口
    driver.switch_to.window(driver.current_window_handle)
    #执行脚本，显示一个框提示用户
    wait_seconds=10
    driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","\v"),wait_seconds))
    time.sleep(wait_seconds)
finally:
    driver.quit()



