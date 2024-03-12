from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

class Test:
    # create test cases to check the boot of webpage

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    # create test cases to check the title of webpage

    @pytest.mark.html
    def testTitle(self):
        self.driver.get(data.WebData().url)
        assert self.driver.title == data.WebData().pageTitle
        print("Title verified!")

    # create test cases to check search function

    @pytest.mark.html
    def testSearch(self, boot):
        self.driver.get(data.WebData().url)
        locator.WebLocators().enterText(self.driver, data.WebData().query)
        locator.WebLocators().clickButton(self.driver)
        assert self.driver.current_url == data.WebData().searchPage
        print(f"Successful search for {data.WebData().query} !")


