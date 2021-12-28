
"""
教师管理：查询、重置密码
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

# 点击教师管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_11']").click()
time.sleep(1)
# 点击查询
driver.find_element_by_xpath("//*[@id='search_user']").send_keys("贾")
time.sleep(1)
# 点击重置密码
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[2]/div[2]/"
                             "div[2]/table/tbody/tr[6]/td[9]/div/a").click()
# 关闭当前页面
webdriver.close()

time.sleep(5)
webdriver.quit()

