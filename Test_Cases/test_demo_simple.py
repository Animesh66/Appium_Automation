import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = dict(
    deviceName='Galaxy Note 10',
    platformName='Android',
    platformVersion='11',
    app='/Users/animeshmukherjee/PycharmProjects/pythonProject/Appium_Automation/Android_App/Simple DEMO_org.simple.clinic.staging.apk',
    automationName='UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.find_element_by_id("org.simple.clinic.staging:id/nextButton").click()
driver.find_element_by_id("org.simple.clinic.staging:id/getStartedButton").click()
driver.find_element_by_xpath("//android.widget.RadioButton[@text='India']").click()
wait.until(EC.element_to_be_clickable(By.ID, "org.simple.clinic.staging:id/nextButton"))
driver.find_element_by_id("org.simple.clinic.staging:id/nextButton").click()
driver.find_element_by_id("org.simple.clinic.staging:id/phoneNumberEditText").send_keys("8123456789")
driver.find_element_by_id("org.simple.clinic.staging:id/nextButton").click()
driver.find_element_by_id("org.simple.clinic.staging:id/fullNameEditText").send_keys("Mamam")
driver.find_element_by_id("org.simple.clinic.staging:id/nextButton").click()
driver.find_element_by_id("org.simple.clinic.staging:id/pinEditText").send_keys("1234")
driver.find_element_by_id("org.simple.clinic.staging:id/confirmPinEditText").send_keys("1234")
driver.find_element_by_id("org.simple.clinic.staging:id/skipButton").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='CC Pinecone']").click()
driver.find_element_by_id("org.simple.clinic.staging:id/yesButton").click()
driver.find_element_by_id("org.simple.clinic.staging:id/skipButton").click()
time.sleep(3)
driver.quit()
