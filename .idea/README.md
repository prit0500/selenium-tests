# Selenium Automation Tests for LambdaTest Assignment

## Overview
This repository contains a suite of automated tests developed in Python using Selenium WebDriver. These tests validate key functionalities on LambdaTest's Selenium Playground and run across multiple browsers and platforms using LambdaTest Cloud Selenium Grid.

The test scenarios include:
- **Simple Form Demo:** Verify that an entered message is correctly displayed.
- **Drag & Drop Sliders:** Adjust the slider to a target value (95) and confirm the update.
- **Input Form Submit:** Validate form submission by checking for proper error messages and a success message after filling in all required fields.

## Table of Contents
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Test Scenarios](#test-scenarios)
- [Artifacts](#artifacts)
- [Gitpod Configuration](#gitpod-configuration)
- [Submission Guidelines](#submission-guidelines)
- [Contributing](#contributing)
- [License](#license)

## Installation & Setup

### Prerequisites
- Python 3.x
- Git
- PyCharm (or your preferred IDE)
- A LambdaTest account

### Dependencies
Install the required packages by running:
```bash
pip install -r requirements.txt

Usage
Running Tests Locally
To run tests using pytest, execute:

pytest --maxfail=1 --disable-warnings -q

Alternatively, if you are using unittest, run:

python -m unittest discover

Parallel Execution

If you want to run tests in parallel with pytest, use:

pytest -n auto
This command automatically distributes tests across available processors.

Test Scenarios
Simple Form Demo:

Description: Navigate to the Simple Form Demo page, input a message, and verify that the message appears correctly under "Your Message".
Expected Result: The displayed message matches the input.
Drag & Drop Sliders:

Description: Navigate to the Drag & Drop Sliders page, adjust the slider so that its value becomes 95, and verify the update.
Expected Result: The slider's displayed value is updated to 95.
Input Form Submit:

Description: Navigate to the Input Form Submit page, first attempt to submit the form without filling any fields to check for validation errors, then fill in all required fields (including selecting "United States" from a dropdown) and submit the form.
Expected Result: An error message appears when fields are empty and, after filling in, a success message ("Thanks for contacting us, we will get back to you shortly.") is displayed.
Artifacts
During test execution on LambdaTest, the following artifacts are captured:

Logs: Detailed logs of test execution.
Screenshots: Taken on test failures and at key checkpoints.
Video Recordings: Complete video recordings of the test sessions.
These artifacts can be viewed on the LambdaTest dashboard.

Gitpod Configuration
This repository includes a .gitpod.yml file that sets up a ready-to-use development environment on Gitpod. Simply open the repository in Gitpod to launch an instant workspace