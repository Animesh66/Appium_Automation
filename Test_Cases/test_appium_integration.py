import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


def get_data():
    return [
        ["animesh5678@gmail.com", "Welcome@1"],
        ["er.animesh6@gmail.com", "Welcome@2"],
        ["er.animesh6@hotmail.com", "Welcome@3"]
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
        automationName='UiAutomator2'
    )
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
    driver.implicitly_wait(10)


def teardown_function(function):
    driver.quit()
    appium_service.stop()


@pytest.mark.parametrize("username, password", get_data())
def test_goibibo(username, password):
    pass
