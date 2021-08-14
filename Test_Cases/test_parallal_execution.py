import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import openpyxl as xl


@pytest.fixture(params=["device1", "device2"], scope="function")
def appium_driver(request):
    if request.param == "device1":
        desired_cap = dict(
            deviceName='Galaxy Note 10',
            platformName='Android',
            platformVersion='11',
            appPackage='com.instagram.android',
            udid='R58M86QW34P',
            appActivity='com.instagram.mainactivity.MainActivity',
            automationName='UiAutomator2',
            noReset=False
        )
        driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', desired_cap)

    if request.param == "device2":
        desired_cap = dict(
            deviceName='Nexus 7',
            platformName='Android',
            platformVersion='8.1',
            appPackage='com.instagram.android',
            udid='emulator-5554',
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
    # driver.find_element_by_id("com.instagram.android:id/sign_up_with_email_or_phone").click()
    # assert "Test" in str(city).upper()
    # allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
