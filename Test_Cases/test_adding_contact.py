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
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.Button[@content-desc='Create contact']")
driver.find_element_by_id("com.samsung.android.app.contacts:id/check").click()
driver.find_element_by_id("android:id/button2").click()
driver.find_element_by_id("com.samsung.android.app.contacts:id/nameEdit").send_keys("John")
driver.find_element_by_id("com.samsung.android.app.contacts:id/titleLayout").send_keys("7979878971")
driver.hide_keyboard()
driver.find_element_by_id("//android.widget.Button[@content-desc='Save']/android.view.ViewGroup/android.widget.TextView").click()
time.sleep(5)
driver.quit()