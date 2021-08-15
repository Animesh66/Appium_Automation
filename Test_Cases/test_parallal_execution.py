import pytest
from appium import webdriver


@pytest.fixture(params=["note_10", "nexus_7"], scope="function")
def appium_driver(request):

    if request.param == 'note_10':
        desired_cap = dict(
            deviceName='Galaxy Note 10',
            platformName='Android',
            platformVersion='11',
            udid='R58M86QW34P',
            appPackage='com.instagram.android',
            appActivity='com.instagram.mainactivity.MainActivity',
            automationName='UiAutomator2',
            noReset=False
        )
        driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', desired_cap)

    if request.param == 'nexus_7':
        desired_cap = dict(
            deviceName='Nexus 7',
            platformName='Android',
            platformVersion='8.1',
            udid='emulator-5554',
            appPackage='com.instagram.android',
            appActivity='com.instagram.mainactivity.MainActivity',
            automationName='UiAutomator2',
            noReset=False
        )
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_cap)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_instagram(appium_driver):
    driver = appium_driver
    driver.find_element_by_id("com.google.android.gms:id/cancel").click()


