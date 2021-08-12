from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    appPackage='com.freecharge.android',
    appActivity='com.freecharge.fclogin.login.LoginActivity',
    automationName='UiAutomator2'
)

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", desired_cap)
driver.implicitly_wait(10)
driver.find_element_by_id()