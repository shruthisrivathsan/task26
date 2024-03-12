from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Imdb:
    #initialisation
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    #create function to boot up, to wait until boot up and maximise the webpage
    def boot(self):
        self.driver.get(data.WebData().url)
        self.wait.until(EC.url_to_be(data.WebData().url))
        self.driver.maximize_window()

    #create function to quit
    def quit(self):
        self.driver.quit()

    #create function to close the pop up usign the locator created
    def closePopUp(self):
        locator.WebLocators().closePopup(self.driver)

    #create funtion to search for the content using the locators created
    def searchContent(self):
        try:
            self.boot()
            self.closePopUp()
            locator.WebLocators().enterText(self.driver, data.WebData().query)
            locator.WebLocators().clickButton(self.driver)
           # locator.WebLocators().dropDown(self.driver)
            self.wait.until(EC.url_changes(data.WebData().searchPage))
        except NoSuchElementException as e:
            print(f"Error: {e}")
        finally:
            self.quit()

#create an object and call the search content
obj = Imdb()
obj.searchContent()

