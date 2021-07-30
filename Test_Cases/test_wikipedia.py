import time
from appium import webdriver
from selenium.webdriver.support.select import Select

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    browserName='Chrome',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.get("https://www.wikipedia.org/")
dropdown = driver.find_element_by_xpath("//*[@id='searchLanguage']")
select = Select(dropdown)
select.select_by_value("hi")
time.sleep(3)
driver.quit()
