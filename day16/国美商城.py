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

time.sleep(5)
gm.quit()
