import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import openpyxl as xl


def get_data():
    workbook = xl.load_workbook("./data_driven/appium_data.xlsx")
    sheet = workbook["Sheet1"]
    total_rows = sheet.max_row
    total_cols = sheet.max_column
    main_list = []
    for i in range(2, total_rows + 1):
        data_list = []
        for j in range(1, total_cols + 1):
            data = sheet.cell(row=i, column=j).value
            data_list.insert(j, data)
        main_list.insert(i, data_list)
    return main_list


@pytest.fixture(params=["device1", "device2"], scope="function")
def appium_driver(request):
    global appium_service
    global driver
    appium_service = AppiumService()
    appium_service.start()
    driver.implicitly_wait(10)
    if request.param == "device1":
        desired_cap = dict(
            deviceName='Galaxy Note 10',
            platformName='Android',
            platformVersion='11',
            appPackage='com.instagram.android',
            udid='R58M86QW34P',
            appActivity='com.instagram.mainactivity.MainActivity',
            automationName='UiAutomator2',
            noReset=True
        )
        driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', desired_cap)

    if request.param == "device2":
        desired_cap = dict(
            deviceName='Galaxy Note 10',
            platformName='Android',
            platformVersion='11',
            appPackage='com.instagram.android',
            udid='emulator-5554',
            appActivity='com.instagram.mainactivity.MainActivity',
            automationName='UiAutomator2',
            noReset=False
        )
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_cap)

    yield driver
    driver.quit()
    appium_service.stop()


@pytest.mark.parametrize("city, country", get_data())
def test_instagram(city, country):
    driver.find_element_by_id("com.google.android.gms:id/cancel").click()
    #driver.find_element_by_id("com.instagram.android:id/sign_up_with_email_or_phone").click()
    #assert "Test" in str(city).upper()
    #allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
