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
driver.find_element_by_id("flipboard.app:id/account_login_password").send_keys("Maximum9093@")
driver.find_element_by_id("flipboard.app:id/icon_button_text").click()
if driver.find_element_by_id("android:id/button1"):
    driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_id("com.google.android.gms:id/credential_save_reject").click()
driver.find_element_by_id("flipboard.app:id/account_login_full_name").send_keys("Animesh")
driver.find_element_by_id("	flipboard.app:id/account_login_username").send_keys("er.animesh6")
driver.find_element_by_id("	flipboard.app:id/icon_button_text").click()

