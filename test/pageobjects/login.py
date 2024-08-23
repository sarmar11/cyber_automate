from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import InputText, Button


class LoginPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.ID, 'EmailAddress')
        self.password = InputText(By.ID, 'Password')
        self.login_button = Button(By.ID, "Login")
        self.logout_button = Button(By.CLASS_NAME, "logout")

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}/users'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.username.wait_until_visible()
        return self

    def login(self):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        user = {
            'username': self.config.get('Test', 'username'),
            'password': self.config.get('Test', 'password')
        }
        self.username.text = user['username']
        self.password.text = user['password']
        self.login_button.click()
        self.logout_button.wait_until_clickable(10)
