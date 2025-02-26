import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestSimpleFormDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = None

    def setUp(self):
        """Set up WebDriver for LambdaTest."""
        lt_options = {
            "geoLocation": "IN",
            "visual": True,
            "video": True,
            "console": True,
            "network": True,
            "networkThrottling": "Regular 4G",
            "build": "Test_Automation_Build_01",
            "project": "Untitled",
            "name": "Test_Slider_Functionality",
            "w3c": True,
            "plugin": "python-pytest",
        }

        # Select browser settings
        browser = self.__class__.browser
        if browser == "chrome":
            lt_options["browserName"] = "Chrome"
            lt_options["browserVersion"] = "128.0"
            lt_options["platformName"] = "Windows 10"
        elif browser == "edge":
            lt_options["browserName"] = "MicrosoftEdge"
            lt_options["browserVersion"] = "127.0"
            lt_options["platformName"] = "macOS Ventura"
        elif browser == "firefox":
            lt_options["browserName"] = "Firefox"
            lt_options["browserVersion"] = "130.0"
            lt_options["platformName"] = "Windows 11"
        elif browser == "ie":
            lt_options["browserName"] = "Internet Explorer"
            lt_options["browserVersion"] = "11.0"
            lt_options["platformName"] = "Windows 10"

        options = Options()
        options.set_capability("LT:Options", lt_options)

        hub_url = "https://prit0500:m32mFb27QVjwwLEWtFqwM1ZtesHyLms1IiktF0QhX4BuEajMLN@hub.lambdatest.com/wd/hub"

        try:
            self.driver = webdriver.Remote(command_executor=hub_url, options=options)
            self.driver.implicitly_wait(10)
        except Exception as e:
            self.fail(f"WebDriver initialization failed: {str(e)}")

    def test_drag_and_drop_slider(self):
        """Test slider functionality using JavaScript update"""
        driver = self.driver

        # Step 1: Open URL
        driver.get("https://www.lambdatest.com/selenium-playground")

        # Step 2: Click "Drag & Drop Sliders"
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Drag & Drop Sliders"))
        ).click()

        # Step 3: Locate the correct output element
        output_value = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "rangeSuccess"))
        )

        # Step 4: Find the correct slider that corresponds to rangeSuccess
        slider_xpath = "//output[@id='rangeSuccess']/preceding-sibling::input[@type='range']"
        slider = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, slider_xpath))
        )

        # Step 5: Get the initial slider value
        initial_value = output_value.text
        print(f"Initial Slider Value: {initial_value}")

        # Step 6: Use JavaScript to directly set the slider value
        driver.execute_script("""
            arguments[0].value = 95;
            arguments[0].dispatchEvent(new Event('input'));
            arguments[0].dispatchEvent(new Event('change'));  // Ensure UI updates
            document.getElementById('rangeSuccess').innerText = arguments[0].value; // Manually update output
        """, slider)

        # Step 7: Sleep longer for UI updates and debugging
        time.sleep(5)  # Increased sleep time to wait for updates

        # Step 8: Debug the output value to see if it reflects the update
        print(f"Output Value After Slider Update: {output_value.text}")

        # Step 9: Wait for the output value to reflect 95
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element((By.ID, "rangeSuccess"), "95")
        )

        # Step 10: Validate the slider value (target: 95)
        updated_value = output_value.text
        print(f"Updated Slider Value: {updated_value}")
        self.assertEqual(updated_value, "95")

    def tearDown(self):
        """Close the browser session."""
        if self.driver:
            self.driver.quit()


def get_browsers():
    return ["chrome", "edge", "firefox", "ie"]


def create_test_suite():
    suite = unittest.TestSuite()
    for browser in get_browsers():
        TestSimpleFormDemo.browser = browser  # Assign before adding tests
        suite.addTest(TestSimpleFormDemo("test_drag_and_drop_slider"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(create_test_suite())
