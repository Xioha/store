'''
    selenium:


'''
# from unittest import TestCase
from selenium import webdriver
import time


# class TestHkr:

    # def testLogin(self):
        #
username = "liujunhao"
password = "qaz123"
        # expect = "Student Login"  # 浏览器标题信息当成登陆成功依据

driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
driver.find_element_by_xpath("//*[@id='submit']").click()

# 点击头像
driver.find_element_by_xpath("//*[@id='img']").click()
time.sleep(1)
# 上传头像
driver.find_element_by_xpath("//*[@id='lablefile']").click()
# driver.get(open('1.jpg').read())


# 关闭当前页面
webdriver.close()

time.sleep(5)
webdriver.quit()

