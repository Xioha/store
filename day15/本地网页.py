from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get(r"F:\作业\day15\练习的html\滑动验证\mousedrag.html")
try:
    a=driver.find_element_by_xpath("/html/body/div/div/fguioihgfgh")#把滑块打包
    ac=ActionChains(driver)#把driver交给事件链执行
    # ac来驱动鼠标  点住 滑块包. 从300滑倒0   .立即执行
    ac.click_and_hold(a).move_by_offset(300,0).perform()#立即执行
except:
    driver.save_screenshot("a.png")

time.sleep(5)
driver.quit()
