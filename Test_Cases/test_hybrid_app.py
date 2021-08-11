import time

from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    appPackage='com.android.chrome',
    appActivity='org.chromium.chrome.browser.ChromeTabbedActivity',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
driver.get("https://www.google.com")
time.sleep(3)
contexts = driver.contexts  # get the context of the hybrid app
for context in contexts:
    print(context)
driver.switch_to.context("WEBVIEW_chrome")
driver.find_element_by_id("com.android.chrome:id/search_box_text").send_keys("Hello Appium")
