from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers


class X_Page:
   # AUTH PAGE
      EMAIL_A_FIELD = (By.ID, 'x')
      PASS_FIELD = (By.XPATH, 'x')
      LOGIN_BUTT = (By.CLASS, 'x')
      FEED_A_FIELD = (By.)
   # FORM SUB PAGE
      NAME_FIELD = 
      EMAIL_FS_FIELD = 
      CN_FIELD =
      DATE_FIELD =
      UPLOAD_BUTT =
      COLOR_BUTT =
      FOOD_BUTT = 
      COUNTRY_DROP = 
      COUNTRY_BUTT = 
      FEED_FS_FIELD =()
   # DND PAGE
      
      
      def __init__(self, driver):
         self.driver = driver  # Initialize the driver
# AUTH PAGE
      def enter_info(self, email_text, pass_text):
         self.driver.find_element(*self.EMAIL_A_FIELD).send_keys(email_text)
         self.deiver.find_wlememt(*self.PASS_FIELD).send_keys(pass_text)
         WebDriverWait(self.driver, 10).until( expected_conditions.visibility_of_element_located(self.X_LOCATOR))
         self.driver.find_element(*self.LOGIN_BUTT).click()
      
      def enter_feedback(self, feed_text):
         self.driver.find_element(*self.FEED_A_FIELD).send_keys(feed_text)
        return self.driver.find_element(*self.FEED_A_FIELD).get_property("textContent")
