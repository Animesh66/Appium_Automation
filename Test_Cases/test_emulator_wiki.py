import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.select import Select

desired_cap = dict(
    deviceName='Nexus 5X',
    platformName='Android',
    platformVersion='8.1',
    browserName='Chrome',
    automationName='UiAutomator2'
)
appium_service = AppiumService()  # create Appium object
appium_service.start(env={'ANDROID_HOME': '/Users/animeshmukherjee/Library/Android/sdk',
                          'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk1.8.0_291.jdk/Contents/Home'
                          }
                     )  # start Appium connection
print(appium_service.is_running)
print(appium_service.is_listening)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.get("https://www.wikipedia.org/")
dropdown = driver.find_element_by_xpath("//*[@id='searchLanguage']")
select = Select(dropdown)
select.select_by_value("hi")
options = driver.find_elements_by_tag_name("option")
no_of_dropdown = len(options)
print(f"number of values are {no_of_dropdown}")
for option in options:
    print(f"Text is {option.text} language is {option.get_attribute('Lang')}")
time.sleep(3)
driver.quit()
appium_service.stop()  # stop Appium connection
