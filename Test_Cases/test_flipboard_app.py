import time
from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    appPackage='flipboard.app',
    appActivity='flipboard.activities.AccountLoginActivity',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
driver.find_element_by_id("flipboard.app:id/account_login_email_button").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='animesh5678@gmail.com']").click()