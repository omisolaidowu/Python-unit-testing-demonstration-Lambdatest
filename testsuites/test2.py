import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner

from unittest import TestCase

import sys
sys.path.append(sys.path[0] + "/..")
from setup.setup import testSet
from locators.testLocators import Locator

from locators.testLocators import webActions

set_up = testSet()
# locate = Locator()
webAction = webActions(set_up.driver)
class FirstSampleTest(unittest.TestCase):
    def test_unit_user_should_able_to_add_item(self):
        try:
            webAction.getWeb("https://todomvc.com/examples/react/#/")
            title = webAction.getTitle()
            self.assertIn("Todo", title, "Todo is not in title")
            webAction.addTask("Omisola")
            webAction.completeTask()
            webAction.clearTask()
        except AssertionError as e:
            print("Something went wrong", e)

        set_up.tearDown()

if __name__ == "__main__":
    
    unittest.main()