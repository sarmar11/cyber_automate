from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import Button, InputText


class XSSLabPageObject(PageObject):
    def init_page_elements(self):
        self.access_lab = Button(By.CLASS_NAME, 'button-orange')
        self.form_input = InputText(By.XPATH, '//form/input')
        self.form_search = Button(By.XPATH, '//form/button')
        self.alert = Alert(self.driver)

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get(f'{self.config.get("Test", "url")}/{self.config.get("Test", "xss_lab_1")}')
        self.access_lab.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self

    def wait_until_loaded(self):
        """ Wait until xss lab page is loaded

        :returns: this page object instance
        """
        self.form_input.wait_until_visible()
        return self

    def search_form(self, text):
        """ Fill login form and submit it

        :param text: value to search
        :returns: secure area page object instance
        """
        self.form_input.text = text
        self.form_search.click()

    def alert_visibility(self):
        try:
            self.alert.text
            return True
        except NoAlertPresentException:
            return False

