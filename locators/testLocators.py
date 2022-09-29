from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
from unittest import TestCase
sys.path.append(sys.path[0] + "/..")
from setup.setup import testSet

set_up = testSet()

class Locator:
    
    addTodo = "new-todo"
    completeTodo = "toggle"
    clearTodo = "clear-completed"

locate = Locator()
# driver = set_up.driver

class webActions:
    def __init__(self, driver) -> None:
        self.driver=driver

    def getWeb(self, URL):
        self.driver.get(URL)

    def getTitle(self):
        self.driver.title

    def addTask(self, task):
        self.driver.find_element(By.CLASS_NAME, locate.addTodo).send_keys(task, Keys.ENTER)

    def completeTask(self):
        self.driver.find_element(By.CLASS_NAME, locate.completeTodo).click()

    def clearTask(self):
        self.driver.find_element(By.CLASS_NAME, locate.clearTodo).click()
    



