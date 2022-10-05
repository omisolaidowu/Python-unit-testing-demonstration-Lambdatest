from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class todoLocator:
    addTodo = "new-todo"
    completeTodo = "toggle"
    clearTodo = "clear-completed"

locateTodo = todoLocator()
# driver = set_up.driver

class todoWebActions:
    def __init__(self, driver) -> None:
        self.driver=driver

    def getWeb(self, URL):
        self.driver.get(URL)

    def getTitle(self):
        return self.driver.title

    def addTask(self, task):
        self.driver.find_element(By.CLASS_NAME, locateTodo.addTodo).send_keys(task, Keys.ENTER)

    def completeTask(self):
        self.driver.find_element(By.CLASS_NAME, locateTodo.completeTodo).click()

    def clearTask(self):
        self.driver.find_element(By.CLASS_NAME, locateTodo.clearTodo).click()
    



