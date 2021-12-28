
"""
a)	用户注册
"""


from selenium import webdriver
import time

username = "tonghe"
password = "root"
# 打开网页
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.maximize_window()



# 注册新用户
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
time.sleep(1)
# 登录名
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("xiao")
# 真实姓名
driver.find_element_by_xpath("/html/body/form/fieldset[1]/input[2]").send_keys("肖")
# 密码
driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123456")
# 确认密码
driver.find_element_by_xpath("/html/body/form/fieldset[1]/input[4]").send_keys("123456")
time.sleep(1)
# 点击下一步
driver.find_element_by_xpath("/html/body/form/fieldset[1]/input[5]")
time.sleep(1)
# 基本信息
driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("28")
driver.find_element_by_xpath('/html/body/form/fieldset[2]/select[1]').send_keys([1])
driver.find_element_by_xpath("//*[@id='classname']").send_keys([1])
# 下一步
driver.find_element_by_xpath("/html/body/form/fieldset[2]/input[3]")
time.sleep(1)
# 联系方式
driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys('123@qq.com')
driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys('13201012345')
driver.find_element_by_xpath("/html/body/form/fieldset[3]/textarea").send_keys("昌平区")
# 注册
driver.find_element_by_xpath("//*[@id='btn_reg']").click()
# 关闭当前页面
webdriver.close()

time.sleep(3)
webdriver.quit()

