class ScrollUtil:

    @staticmethod
    def scroll_to_text_by_UiAutomator(text, driver):
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true)."
                                                   "instance(""0)).scrollIntoView(new UiSelector()"
                                                   ".textContains(\"" + text + "\").instance(0))").click()

    @staticmethod
    def swipe_up(no_of_swipes, driver):
        for i in range(1, no_of_swipes+1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipe_down(no_of_swipes, driver):
        for i in range(1, no_of_swipes+1):
            driver.swipe(514, 500, 514, 800, 1000)
