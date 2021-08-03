import time

from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    app='/Users/animeshmukherjee/PycharmProjects/pythonProject/Appium_Automation/Android_App/CallHippo_com.callhippo.bueno.callhippo.apk',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
time.sleep(3)
driver.quit()