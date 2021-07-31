import time
from appium import webdriver


desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
time.sleep(5)
driver.quit()
