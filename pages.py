from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers


class X_Page:
    LOCATOR = (By.ID, 'x')
    LOCATOR = (By.XPATH, 'x')
    LOCATOR = (By.CLASS, 'x')
   
   
   def __init__(self, driver):
        self.driver = driver  # Initialize the driver

       def enter_locations(self, x_text):
        self.driver.find_element(*self.X_LOCATOR).send_keys(x_text)
        WebDriverWait(self.driver, 10).until( expected_conditions.visibility_of_element_located(self.X_LOCATOR))
        self.driver.find_element(*self.CALL_BUTTON_LOCATOR).click()
      
      def get_phone_number_field_value(self):
        return self.driver.find_element(*self.PHONE_BUTTON_LOCATOR).get_property("textContent")
