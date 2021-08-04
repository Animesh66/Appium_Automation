import time

from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    appPackage='com.samsung.android.app.contacts',
    appActivity='com.samsung.android.contacts.contactslist.PeopleActivity',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.swipe(510, 600, 510, 200, 1000)
driver.swipe(510, 600, 510, 200, 1000)
driver.swipe(510, 600, 510, 200, 1000)
driver.swipe(510, 600, 510, 200, 1000)
time.sleep(2)
driver.swipe(510, 500, 510, 1000, 1000)
driver.swipe(510, 500, 510, 1000, 1000)
driver.swipe(510, 500, 510, 1000, 1000)
driver.swipe(510, 500, 510, 1000, 1000)