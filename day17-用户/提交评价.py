"""
提交评价
"""
from selenium import webdriver
import time

username = "liujunhao"
password = "qaz123"

driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
driver.find_element_by_xpath("//*[@id='submit']").click()

# 点击提交评价
driver.find_element_by_xpath("//*[@id='subtn']").click()
time.sleep(1)
# 关闭当前页面
webdriver.close()

time.sleep(5)
webdriver.quit()

