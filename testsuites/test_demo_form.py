import unittest
import HtmlTestRunner

import sys
sys.path.append(sys.path[0] + "/..")
from setup.setup import testSet

from locators.formLocators import formWebAction

set_up = testSet()
form = formWebAction(set_up.driver)

class TodoSampleTest(unittest.TestCase):
    def test_unit_user_should_able_to_add_item(self):
        try:
            form.getWeb("https://www.lambdatest.com/selenium-playground/input-form-demo")
            title = form.getTitle()
            self.assertIn("Seleniu", title, "Seleniu is not in title")

            form.fillName("Idowu")
            form.fillEmail("fakeemail@gmail.com")
            form.fillPassword("secret")
            form.fillCompany("Lambdatest")
            form.fillWebsite("someweb.com")
            form.fillCountry("Nigeria")
            form.fillCity("A City")
            form.fillAddress1("Den street")
            form.fillAddress2("Den street")
            form.fillState("Lagos")
            form.fillZipCode("240100")
            form.submit()
            
        except AssertionError as e:
            print("Something went wrong", e)

        set_up.tearDown()

if __name__ == "__main__":
    
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='DemoFormHTML_results'))