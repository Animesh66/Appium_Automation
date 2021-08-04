class ScrollToText:

    @staticmethod
    def scroll_to_text_by_UiAutomator(text, driver):
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true)."
                                                   "instance(""0)).scrollIntoView(new UiSelector()"
                                                   ".textContains(\""+ text + "\").instance(0))").click()
    @staticmethod
    def swipe_up(no_of_swipes, driver):
        pass


    def swipe_down(no_of_swipes, driver):
        pass
