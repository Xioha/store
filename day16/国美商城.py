from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

gm = webdriver.Chrome()
gm.get("https://www.gome.com.cn/")  # 进入国美商城网站
ac = ActionChains(gm)  # 控制鼠标
a = gm.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div/ul/li[11]/h3/a[1]')  # 鼠标悬浮在此处
ac.move_to_element(a).perform()
gm.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[2]/div/div[11]/div[1]/div[2]/div[1]/ul/div[2]/a[1]").click()  # 进入鼠标所在位置
time.sleep(3)
# 切换当前页面
# 点击进入商品页面
handles = gm.window_handles
gm.switch_to.window(handles[-1])
gm.find_element_by_xpath("/html/body/div[10]/div/div[2]/div[3]/ul/li[1]/div/div/p[1]/a/img").click()
# 切换当前页面
# 点击加入购物车
handles = gm.window_handles
gm.switch_to.window(handles[-1])
gm.find_element_by_xpath("/html/body/div[7]/div[2]/div[7]/a[4]").click()
time.sleep(3)
# 点击我的购物车
gm.find_element(By.XPATH,"/html/body/div[5]/div/div/div[3]/a[2]").click()
# 点击结算
gm.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div[6]/a/span").click()
time.sleep(10)
# 关闭当前页面
gm.close()

time.sleep(5)
gm.quit()
