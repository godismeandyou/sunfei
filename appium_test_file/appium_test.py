# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import time
import _device
from appium.webdriver.common.touch_action import TouchAction


def sleep(a):
    aa = time.sleep(a)
    return aa

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
sleep(3)
el1 = driver.find_element_by_id("linkpage_start_register")
el1.click()
el2 = driver.find_element_by_id("tv_other")
el2.click()
el3 = driver.find_element_by_id("etUserName")
el3.send_keys("sunfei10")
el4 = driver.find_element_by_id("etPassword")
el4.send_keys("123456")
el5 = driver.find_element_by_id("ll_submit")
el5.click()
sleep(2)

unlock_jiu()

sleep(10)
driver.quit()






