
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from pathlib import Path
from datetime import date
from Constants import constants



class Test_AddCostumer():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get(constants.URL)
    self.driver.maximize_window()
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  

  def teardown_method(self, method):
    self.driver.quit()

  def WaitForElementVisible(self,locator,timeout=5):
    WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

  def test_addCostumer(self):
    self.WaitForElementVisible((By.XPATH,constants.customerBtn_XPATH))
    customerBtn = self.driver.find_element(By.XPATH,constants.customerBtn_XPATH)
    customerBtn.click()
    self.WaitForElementVisible((By.ID,constants.yourName_ID))
    yourName= self.driver.find_element(By.ID,constants.yourName_ID)
    drop = Select(yourName)
    drop.select_by_visible_text("Hermoine Granger")
    self.driver.save_screenshot(f"{self.folderPath}/test-addcustomers.png")
    self.WaitForElementVisible((By.XPATH,constants.loginBtn_XPATH))
    loginBtn = self.driver.find_element(By.XPATH,constants.loginBtn_XPATH)
    loginBtn.click()