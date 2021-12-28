"""
修改个人信息
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

# 点击修改个人信息
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/li[1]/ul/li/div/span[4]/a").click()
time.sleep(1)
# 点击修改
driver.find_element_by_xpath("//*[@id='btn_modify']").click()
# 关闭当前页面
webdriver.close()

time.sleep(5)
webdriver.quit()

