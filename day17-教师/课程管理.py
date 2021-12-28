
"""
b)	学生管理：姓名和电话号码查询、设置毕业和未毕业状态
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

# 点击课程管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_13']").click()
time.sleep(1)
# 点击添加
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/table"
                             "/tbody/tr/td/a/span/span[1]").click()
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a[1]/span/span[1]").click()
time.sleep(1)
# 点击取消添加
driver.find_element_by_xpath("/html/body/div[10]/div[3]/a/span/span").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a[2]/span/span[1]").click()

# 关闭当前页面
webdriver.close()

time.sleep(3)
webdriver.quit()

