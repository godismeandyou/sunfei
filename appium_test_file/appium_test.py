# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def sleep(a):
    aa = time.sleep(a)
    return aa

caps = {}
caps["platformName"] = "android"
caps["appPackage"] = "com.iqianjin.client"
caps["appActivity"] = ".asurface.activity.StartActivity"
caps["deviceName"] = "demo"
caps["NoReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
sleep(5)
el1 = driver.find_element_by_id("com.iqianjin.client:id/linkpage_start_register")
el1.click()
el2 = driver.find_element_by_id("com.iqianjin.client:id/tv_other")
el2.click()
el3 = driver.find_element_by_id("com.iqianjin.client:id/etUserName")
el3.send_keys("15011518955")
el4 = driver.find_element_by_id("com.iqianjin.client:id/etPassword")
el4.send_keys("sunfei1234")
el5 = driver.find_element_by_id("com.iqianjin.client:id/ll_submit")
el5.click()

# TouchAction(driver)\
#     .press(x=231, y=685).move_to(x=231, y=685).wait(100)\
#     .move_to(x=834, y=685).wait(100)\
#     .move_to(x=849, y=685).wait(100)\
#     .move_to(x=849,y=988)\
#     .release().perform()

sleep(10)
driver.quit()