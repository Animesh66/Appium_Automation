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
driver.find_element_by_xpath("//input[@id='m_login_email']").send_keys("animesh@abc.com")
time.sleep(3)
driver.quit()
