import data
import helpers
from selenium import webdriver

from pages import X_Page
class TestX:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.WEBSITE_URL):
            print("Connected to the Test server")
        else:
            print("Cannot connect to Test server. Check the server is on and still running")
    def test_auth(self):
        self.driver.get(data.WEBSITE_URL)
        test_page = TestPage(self.driver)
        test_page.enter_info(data.E_VALUE, data.P_VALUE)
        assert test_page.get_email() == data.E_VALUE
        assert test_page.get_pass() == data.P_VALUE
        test_page.enter_feed(data.FEED_VALUE)
        assert test_page.get_feed() == data.FEED_VALUE
    def test_feed(self):
        self.driver.get(data.WEBSITE_URL)
        test_page = TestPage(self.driver)
        test_page.enter_feed(data.FEED_VALUE)
        assert test_page.get_feed() == data.FEED_VALUE