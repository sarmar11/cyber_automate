from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import Button, PageElement, PageElements


class SQLiLabPageObject(PageObject):
    def init_page_elements(self):
        self.access_lab = Button(By.CLASS_NAME, 'button-orange')
        self.search_filters = PageElement(By.CLASS_NAME, 'search-filters')
        self.list_titles = PageElements(By.XPATH, '//section[@class="container-list-tiles"]/div')
        self.alert = Alert(self.driver)

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get(f'{self.config.get("Test", "url")}/{self.config.get("Test", "sqli_lab_1")}')
        self.access_lab.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self

    def wait_until_loaded(self):
        """ Wait until sqli lab page is loaded

        :returns: this page object instance
        """
        self.search_filters.wait_until_visible()
        return self

    def force_url_sqli(self, sqli_str):
        """ Fill login form and submit it

        :param sqli_str: value to search
        :returns: secure area page object instance
        """
        current_url = self.driver.current_url
        self.driver.get(f'{current_url}{sqli_str}')



