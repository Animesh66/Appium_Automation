import time
import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


def get_data():
    return [
        ["Delhi"],
        ["Dubai"]
    ]


def setup_function(function):
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_cap = dict(
        deviceName='Galaxy Note 10',
        platformName='Android',
        platformVersion='11',
        appPackage='com.goibibo',
        appActivity='.common.HomeActivity',
        automationName='UiAutomator2',
        noReset=True
    )
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
    driver.implicitly_wait(10)


def teardown_function(function):
    driver.quit()
    appium_service.stop()


@pytest.mark.parametrize("city", get_data())
def test_goibibo(city):
    print(city)
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@content-desc='hotels']/android.widget.TextView").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='getsetgo_clicked']/android.view.ViewGroup/android.widget.TextView").click()
