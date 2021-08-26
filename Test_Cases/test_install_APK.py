import time
from pathlib import Path

from appium import webdriver

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    app=str(Path().absolute().parent) + '/Android_App/CallHippo_com.callhippo.bueno.callhippo.apk',
    # This will return the absolute path of the parent and append it with current path
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
time.sleep(3)
driver.quit()
