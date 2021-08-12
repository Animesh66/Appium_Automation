import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()