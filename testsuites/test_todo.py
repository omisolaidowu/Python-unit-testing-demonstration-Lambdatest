import unittest
import HtmlTestRunner

import sys
sys.path.append(sys.path[0] + "/..")
from setup.setup import testSet

from locators.todoLocators import todoWebActions

set_up = testSet()
todo = todoWebActions(set_up.driver)
class TodoSampleTest(unittest.TestCase):
    def test_unit_user_should_able_to_add_item(self):
        try:
            set_up.testSetup()
            todo.getWeb("https://todomvc.com/examples/react/#/")
            title = todo.getTitle()
            self.assertIn("Todo", title, "Todo is not in title")
            todo.addTask("Omisola")
            todo.completeTask()
            todo.clearTask()
        except AssertionError as e:
            print("Something went wrong", e)

        set_up.tearDown()

if __name__ == "__main__":
    
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='TodoHTML-results'))