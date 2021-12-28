
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

# 点击学生管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_12']").click()
time.sleep(1)
# 点击姓名查询
driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("贾生")
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/table/tbody"
                             "/tr/td[4]/a/span/span[1]").click()
time.sleep(1)
# 点击电话号码查询
driver.find_element_by_xpath("//*[@id='J-phone']").send_keys("1354855")
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/table/tbody"
                             "/tr/td[4]/a/span/span[1]").click()
# 点击设置为毕业
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]"
                             "/div[2]/table/tbody/tr[1]/td[11]/div/a").click()
# 关闭当前页面
webdriver.close()

time.sleep(5)
webdriver.quit()

