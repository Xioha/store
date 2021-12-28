
"""
e)	历史操作日志：日期查询日志，导出当前操作历史
"""


from selenium import webdriver
import time

username = "tonghe"
password = "root"
# 打开网页
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.maximize_window()

# 切换到教师登录
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
time.sleep(1)
# 定位输入框
driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
driver.find_element_by_xpath("//*[@id='submit']").click()

# 历史操作日志
driver.find_element_by_xpath("//*[@id='_easyui_tree_18']").click()
time.sleep(1)
# 查询日志
driver.find_element_by_xpath("//*[@id='J-history']").send_keys("")
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/table"
                             "/tbody/tr/td[2]/a/span/span[1]").click()
time.sleep(1)
# 导出历史
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/table"
                             "/tbody/tr/td[4]/a/span/span[1]").click()
time.sleep(1)

# 关闭当前页面
webdriver.close()

time.sleep(3)
webdriver.quit()

