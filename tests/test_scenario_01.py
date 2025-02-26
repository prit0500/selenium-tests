import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class TestSimpleFormDemo(unittest.TestCase):
    def setUp(self):
        # LambdaTest capabilities
        lt_options = {
            "browserName": "Chrome",
            "browserVersion": "128.0",
            "platformName": "Windows 10",
            "geoLocation": "IN",
            "visual": True,
            "video": True,
            "console": True,
            "network": True,
            "networkThrottling": "Regular 4G",
            "build": "Test_Automation_Build_01",
            "project": "Untitled",
            "name": "Test_Simple_Form_Submission",
            "w3c": True,
            "plugin": "python-pytest",
        }

        # Set the capabilities for Chrome
        options = Options()
        options.set_capability("LT:Options", lt_options)

        # Initialize Remote WebDriver with LambdaTest hub
        self.driver = webdriver.Remote(
            command_executor="https://prit0500:m32mFb27QVjwwLEWtFqwM1ZtesHyLms1IiktF0QhX4BuEajMLN@hub.lambdatest.com/wd/hub",
            options=options,
        )
        self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_simple_form_demo(self):
        driver = self.driver

        # Step 1: Open URL
        driver.get("https://www.lambdatest.com/selenium-playground")

        # Step 2: Click on "Simple Form Demo"
        driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

        # Step 3: Validate that URL contains "simple-form-demo"
        self.assertIn("simple-form-demo", driver.current_url)

        # Step 4: Enter a message in the text box
        message = "Welcome to LambdaTest"
        driver.find_element(By.ID, "user-message").send_keys(message)

        # Step 5: Click on "Get Checked Value"
        driver.find_element(By.ID, "showInput").click()

        # Step 6: Validate the message in the "Your Message" section
        output_message = driver.find_element(By.ID, "message").text
        self.assertEqual(message, output_message)
        time.sleep(5)

    def tearDown(self):
        # Quit the driver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
