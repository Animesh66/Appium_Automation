import time
from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    browserName='Chrome',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.get("https://www.facebook.com/")
page_title = driver.title
print(page_title)
time.sleep(3)
driver.quit()
