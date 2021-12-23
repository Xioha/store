from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("http://www.baidu.com")

# 窗口最大化
chromeDriver.maximize_window()

# 寻找搜索输入框
chromeDriver.find_element_by_id("kw").send_keys("java")

# 点击百度一下按钮
chromeDriver.find_element_by_id("su").click()

time.sleep(3)
# 退出浏览器
chromeDriver.quit()


# from selenium import webdriver
# import time
#
#
# diver=webdriver.Chrome()
# diver.get("https://mail.qq.com/")
#
# a=diver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").text
# if a=="微信登录":
#     print("用例通过")
# diver.switch_to.frame("login_frame")
# diver.find_element_by_id("u").send_keys("123")
#
# # diver.maximize_window()
# # diver.find_element_by_id("kw").send_keys("迪迦")
# # diver.find_element_by_id("su").click()
# # #
# # diver.find_element_by_xpath("//*[@id='hotsearch-content-wrapper']/li[1]/a/span[2]")
# #/html/body/div[1]/div[1]/div[5]/div/div/div[3]/ul/li[1]/a/span[2]
# #body//////每一步都需要找到才能定位到你元素
#
#
# time.sleep(5)
# diver.quit()
