from selenium import webdriver

from dotenv import load_dotenv
import os
load_dotenv('.env')

username = os.getenv("grid_username")
access_key = os.getenv("access_key")

desired_caps = {
		'LT:Options' : {
			"user" : os.getenv("grid_username"),
			"accessKey" : os.getenv("access_key"),
			"build" : "FireTest New",
			"name" : "FireBrowser",
			"platformName" : os.getenv("test_OS")
		},
		"browserName" : "FireFox",
		"browserVersion" : "103.0",
	}
gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)

class testSet: 
       
    def __init__(self) -> None:
        self.driver = webdriver.Remote(command_executor=gridURL, desired_capabilities= desired_caps)
        
    def testSetup(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        if (self.driver != None):
            print("Cleaning the test environment")
            self.driver.quit()
