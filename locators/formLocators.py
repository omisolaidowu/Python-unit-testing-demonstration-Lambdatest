from selenium.webdriver.common.by import By

class formLocator:
    name = "//input[@id='name']"
    email = "//input[@id='inputEmail4']"
    password = "//input[@id='inputPassword4']"
    company = "//input[@id='company']"
    website = "//input[@id='websitename']"
    country = "//select[@name='country']"
    city = "//input[@id='inputCity']"
    address_1 = "//input[@id='inputAddress1']"
    address_2 = "//input[@id='inputAddress2']"
    state = "inputState"
    zip_code = "inputZip"
    button = "btn"

locateForm = formLocator()


class formWebAction:
    def __init__(self, driver) -> None:
        self.driver=driver
    def getWeb(self, URL):
        self.driver.get(URL)
    def getTitle(self):
        return self.driver.title
    def fillName(self, data):
        self.driver.find_element(By.XPATH, locateForm.name).send_keys(data)
    def fillEmail(self, data):
        self.driver.find_element(By.XPATH, locateForm.email).send_keys(data)
    def fillPassword(self, data):
        self.driver.find_element(By.XPATH, locateForm.password).send_keys(data)
    def fillCompany(self, data):
        self.driver.find_element(By.XPATH, locateForm.company).send_keys(data)
    def fillWebsite(self, data):
        self.driver.find_element(By.XPATH, locateForm.website).send_keys(data)
    def fillCountry(self, data):
        self.driver.find_element(By.XPATH, locateForm.country).send_keys(data)
    def fillCity(self, data):
        self.driver.find_element(By.XPATH, locateForm.city).send_keys(data)
    def fillAddress1(self, data):
        self.driver.find_element(By.XPATH, locateForm.address_1).send_keys(data)
    def fillAddress2(self, data):
        self.driver.find_element(By.XPATH, locateForm.address_2).send_keys(data)
    def fillState(self, data):
        self.driver.find_element(By.ID, locateForm.state).send_keys(data)
    def fillZipCode(self, data):
        self.driver.find_element(By.ID, locateForm.zip_code).send_keys(data)
    def submit(self):
        self.driver.find_element(By.CLASS_NAME, locateForm.button).click()
    
       
