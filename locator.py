import binascii

from selenium.webdriver.common.by import By

class WebLocators:
    #initialise the class by creating the locators using Xpath and name
    def __init__(self):
        self.popupLocator= "/html/body/div[2]/div/div/div[2]/div/button[2]"
        self.searchboxLocator = "suggestion-search"
        self.buttonLocator= "suggestion-search-button"
        self.dropdownLocator = "//*[@class='ipc-btn__text']"

    #find the pop up element and close it
    def closePopup(self, driver):
        driver.find_element(by=By.XPATH, value=self.popupLocator).click()

    #find the search box and enter text
    def enterText(self, driver, query):
        driver.find_element(by=By.ID, value=self.searchboxLocator).send_keys(query)

    #find the search button and click on it
    def clickButton(self, driver):
        driver.find_element(by=By.ID, value=self.buttonLocator).click()

    #find the drop down list and click on it
    def dropDown(self, driver):
        driver.find_element(by=By.XPATH, value=self.dropdownLocator).click()