import time
from appium import webdriver

desired_cap = dict(

    deviceName='Samsung',
    platformName='Android',
    browserName='Chrome'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.get("https://google.com")
driver.title
time.sleep(2)
driver.quit()

