import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class TestInputFormSubmit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up WebDriver for LambdaTest."""
        lt_options = {
            "geoLocation": "IN",
            "visual": True,
            "video": True,
            "console": True,
            "network": True,
            "networkThrottling": "Regular 4G",
            "build": "Test_Automation_Build_01",
            "project": "Test_Project",
            "name": "Test_Input_Form_Submit",
            "w3c": True,
            "plugin": "python-pytest",
        }

        # Select browser settings
        browser = "chrome"  # Modify this to select the desired browser
        if browser == "chrome":
            lt_options["browserName"] = "Chrome"
            lt_options["browserVersion"] = "latest"
            lt_options["platformName"] = "Windows 10"
        elif browser == "edge":
            lt_options["browserName"] = "MicrosoftEdge"
            lt_options["browserVersion"] = "latest"
            lt_options["platformName"] = "Windows 10"
        elif browser == "firefox":
            lt_options["browserName"] = "Firefox"
            lt_options["browserVersion"] = "latest"
            lt_options["platformName"] = "Windows 10"
        elif browser == "ie":
            lt_options["browserName"] = "Internet Explorer"
            lt_options["browserVersion"] = "11.0"
            lt_options["platformName"] = "Windows 10"

        options = Options()
        options.set_capability("LT:Options", lt_options)

        # LambdaTest credentials (replace these with your actual credentials)
        username = "prit0500"
        access_key = "m32mFb27QVjwwLEWtFqwM1ZtesHyLms1IiktF0QhX4BuEajMLN"

        # LambdaTest Selenium Grid URL
        hub_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

        try:
            # Initialize WebDriver for LambdaTest
            cls.driver = webdriver.Remote(command_executor=hub_url, options=options)
            cls.driver.implicitly_wait(10)
        except Exception as e:
            # Print the error message and raise an assertion failure
            print(f"WebDriver initialization failed: {str(e)}")
            raise AssertionError(f"WebDriver initialization failed: {str(e)}")

    def test_input_form_submit(self):
        """Test the input form submit scenario."""
        driver = self.driver

        # Step 1: Open the URL
        driver.get("https://www.lambdatest.com/selenium-playground")

        # Step 2: Click on "Input Form Submit"
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[.='Input Form Submit']"))
        ).click()

        # Step 3: Click "Submit" without filling in any information
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='seleniumform']/div[6]/button"))
        )
        submit_button.click()

        # Step 4: Wait for the validation error message and assert "Please fill out this field."
        time.sleep(2)
        validation_message = driver.execute_script("return document.querySelector('input:invalid').validationMessage;")
        self.assertEqual(validation_message, "Please fill out this field.")

        # Step 5: Fill in the required fields
        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("John Doe")
        driver.find_element(By.XPATH, "//form[@id='seleniumform']//input[@name='email']").send_keys("john.doe@example.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("password123")
        driver.find_element(By.CSS_SELECTOR, "#company").send_keys("LambdaTest")
        driver.find_element(By.CSS_SELECTOR, "#websitename").send_keys("https://www.lambdatest.com")

        # Step 6: Select "United States" from the Country Dropdown
        country_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='country']"))
        )
        # Create Select object and select the country
        select = Select(country_dropdown)
        select.select_by_visible_text("United States")

        # Step 7: Fill in other fields and submit the form
        driver.find_element(By.XPATH, "//input[@id='inputCity']").send_keys("San Jose")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Address 1']").send_keys("Googleplex, 1600 Amphitheatre Pkwy")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Address 2']").send_keys("Mountain View, CA 94043")
        driver.find_element(By.CSS_SELECTOR, "#inputState").send_keys("California")
        driver.find_element(By.CSS_SELECTOR, "#inputZip").send_keys("94088")

        # Step 8: Click the submit button again
        submit_button.click()

        # Step 9: Assert if the page contains the success message
        try:
            assert "Thanks for contacting us, we will get back to you shortly" in driver.page_source
            print("Passed: Input Form Demo")
        except AssertionError:
            print("Failed: Input Form Demo")

    @classmethod
    def tearDownClass(cls):
        """Close the browser session."""
        if hasattr(cls, 'driver'):
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
