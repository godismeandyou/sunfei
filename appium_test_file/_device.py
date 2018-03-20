from appium import webdriver

def device_a():
    caps = {}
    caps["platformName"] = "android"
    caps["appPackage"] = "com.iqianjin.client"
    caps["appActivity"] = ".asurface.activity.StartActivity"
    caps["deviceName"] = "demo"
    caps["NoReset"] = "true"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    return driver