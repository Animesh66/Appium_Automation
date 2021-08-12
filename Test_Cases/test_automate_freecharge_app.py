import time

from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    appPackage='com.freecharge.android',
    appActivity='com.freecharge.activities.splash.SplashActivity',
    automationName='UiAutomator2'
)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)
driver.find_element_by_id("com.freecharge.android:id/getStarted").click()
driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
driver.find_element_by_id("com.android.permissioncontroller:id/permission_deny_button").click()
driver.find_element_by_id("com.google.android.gms:id/cancel").click()
driver.find_element_by_id("com.freecharge.android:id/username").send_keys("8900560944")
driver.find_element_by_id("com.freecharge.android:id/submit").click()
# switching to messaging app to read the SMS text
driver.start_activity("com.samsung.android.messaging",".ui.view.main.WithActivity")
time.sleep(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='AD-FCHARG']").click()
messages = driver.find_elements_by_id('com.samsung.android.messaging:id/content_text_view')
text = messages[-1]  # read the text of the last message
print(text)
time.sleep(3)
driver.quit()