import time
from appium import webdriver

desired_cap = dict(
    deviceName='Samsung Note 10',
    platformName='Android',
    platformVersion='11',
    udid='R58M86QW34P',
    appPackage='com.samsung.android.app.contacts',
    appActivity='com.samsung.android.contacts.contactslist.PeopleActivity',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', desired_cap)
driver.implicitly_wait(10)
# element = driver.find_elements_by_accessibility_id("Dadu")
# driver.execute_script("arguments[0].ScrollIntoView", element)
# element.click()
time.sleep(5)
driver.quit()


