# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


import time
import _device
from appium.webdriver.common.touch_action import TouchAction

# 获取时间戳
def jietu():
    tamp = int(time.time())
    return tamp

# 九宫格解锁方法
def unlock_jiu():
    view = [77, 530]
    viewed = [1002, 1455]
    x = (viewed[0] - view[0]) / 6
    y = (viewed[1] - view[1]) / 6

    TouchAction(driver) \
        .press(x=142 + x, y=525 + y).wait(1000) \
        .move_to(x=0, y=2 * y).wait(1000) \
        .move_to(x=0, y=2 * y).wait(1000) \
        .move_to(x=2 * x, y=0).wait(1000) \
        .move_to(x=2 * x, y=0).wait(1000) \
        .release().perform()

    time.sleep(3)

    TouchAction(driver) \
        .press(x=142 + x, y=525 + y).wait(1000) \
        .move_to(x=0, y=2 * y).wait(1000) \
        .move_to(x=0, y=2 * y).wait(1000) \
        .move_to(x=2 * x, y=0).wait(1000) \
        .move_to(x=2 * x, y=0).wait(1000) \
        .release().perform()


driver = _device.device_a()
time.sleep(2)
# 点击引导页按钮，进入注册页面
el1 = driver.find_element_by_id("linkpage_start_register")
el1.click()
# 点击进入登录页面
el2 = driver.find_element_by_id("tv_other")
el2.click()
# 输入账号
el3 = driver.find_element_by_id("etUserName")
el3.send_keys("sunfei10")
# 输入密码
el4 = driver.find_element_by_id("etPassword")
el4.send_keys("123456")
time.sleep(2)
# 点击登录
el5 = driver.find_element_by_id("ll_submit")
el5.click()
# 登录完毕，截图
driver.get_screenshot_as_file('D:\\python_test\\img\\%s_login.png' %jietu())
time.sleep(1)
# 解锁九宫格
unlock_jiu()
time.sleep(3)
# 首页截图
driver.get_screenshot_as_file('D:\\python_test\\img\\%s_index.png' %jietu())

time.sleep(10)
driver.quit()
