
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from pathlib import Path
from datetime import date
from Constants import constants


class Test_AddManager():
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


 
  @pytest.mark.parametrize("FirstName , LastName, PostCode",[("Yunus","Basak","30000")])
 
  def test_addManager(self,FirstName,LastName,PostCode):
    self.WaitForElementVisible((By.XPATH,constants.managerBtn_XPATH))
    managerBtn = self.driver.find_element(By.XPATH,constants.managerBtn_XPATH)
    managerBtn.click()
    self.WaitForElementVisible((By.XPATH,constants.customerAdd_XPATH))
    customerAdd = self.driver.find_element(By.XPATH,constants.customerAdd_XPATH)
    customerAdd.click()
    self.WaitForElementVisible((By.XPATH,constants.FirstNameInput_XPATH))
    FirstNameInput = self.driver.find_element(By.XPATH,constants.FirstNameInput_XPATH)
    FirstNameInput.send_keys(FirstName)
    self.WaitForElementVisible((By.XPATH,constants.LastNameInput_XPATH))
    LastNameInput = self.driver.find_element(By.XPATH,constants.LastNameInput_XPATH)
    LastNameInput.send_keys(LastName)
    self.WaitForElementVisible((By.XPATH,constants.PostCodeInput_XPATH))
    PostCodeInput = self.driver.find_element(By.XPATH,constants.PostCodeInput_XPATH)
    PostCodeInput.send_keys(PostCode)
    self.driver.save_screenshot(f"{self.folderPath}/test-add-customer.png")
    self.WaitForElementVisible((By.XPATH,constants.AddCustomer_XPATH))
    AddCustomer = self.driver.find_element(By.XPATH,constants.AddCustomer_XPATH)
    AddCustomer.click()
    alert = Alert(self.driver)
    alert.accept()
    self.WaitForElementVisible((By.XPATH,constants.openAccount_XPATH))
    openAccount = self.driver.find_element(By.XPATH,constants.openAccount_XPATH)
    openAccount.click()
    self.WaitForElementVisible((By.ID,constants.customer_ID))
    customer = self.driver.find_element(By.ID,constants.customer_ID)
    drop = Select(customer)
    drop.select_by_value("6")
    self.WaitForElementVisible((By.ID,constants.currency_ID))
    currency = self.driver.find_element(By.ID,constants.currency_ID)
    drop = Select(currency)
    drop.select_by_value("Dollar")
    self.driver.save_screenshot(f"{self.folderPath}/test-open-account.png")
    self.WaitForElementVisible((By.XPATH,constants.Process_XPATH))
    Process = self.driver.find_element(By.XPATH,constants.Process_XPATH)
    Process.click()
    alert = Alert(self.driver)
    alert.accept()
    self.WaitForElementVisible((By.XPATH,constants.customers_XPATH))
    customers = self.driver.find_element(By.XPATH,constants.customers_XPATH)
    customers.click()
    self.driver.implicitly_wait(2)
    searchCustomer = self.driver.find_element(By.XPATH,constants.searchCustomer_XPATH)
    searchCustomer.send_keys("Harry")
    self.driver.save_screenshot(f"{self.folderPath}/test-customers.png")
    self.WaitForElementVisible((By.XPATH,constants.deleteBtn_XPATH))
    deleteBtn = self.driver.find_element(By.XPATH,constants.deleteBtn_XPATH)
    deleteBtn.click()
    self.WaitForElementVisible((By.XPATH,constants.btnHome_XPATH))
    btnHome = self.driver.find_element(By.XPATH,constants.btnHome_XPATH)
    btnHome.click()

