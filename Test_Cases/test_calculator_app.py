import time

from appium import webdriver

desired_cap = {
    'deviceName': 'Galaxy Note 10',
    'platformName': 'Android',
    'platformVersion': '11',
    'appPackage': 'com.sec.android.app.popupcalculator',
    'appActivity': '.Calculator',
    'automationName': 'UiAutomator2'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.Button[@index='10']").click()
driver.find_element_by_xpath("//android.widget.Button[@index='12']").click()
driver.find_element_by_xpath("//android.widget.Button[@index='15']").click()
driver.find_element_by_xpath("//android.widget.Button[@index='4']").click()
driver.find_element_by_xpath("//android.widget.Button[@index='6']").click()
driver.find_element_by_xpath("//android.widget.Button[@index='19']").click()
result = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_tv_result").text
print(result)
assert int(result) == 140
time.sleep(3)
driver.quit()