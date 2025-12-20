[![Playwright Tests](https://github.com/qascenarios/automationexercise-ii/actions/workflows/playwright-allure.yml/badge.svg)](https://github.com/qascenarios/automationexercise-ii/actions/workflows/playwright-allure.yml)

# Pytest-Playwright Partial End-to-End Tests – Automation Exercise

This repository contains **partial end-to-end (E2E) tests** written using **pytest-playwright** for 
the Automation Exercise application, with a focus on register, login, and cart functionality.

**Application under test:** [https://automationexercise.com](https://automationexercise.com/)

## Project Overview

The purpose of this project is to validate key user flows in the Automation Exercise using 
**Python-based browser automation**. The tests simulate real user interactions to 
ensure that critical cart features behave correctly across different browsers.

This project uses **pytest** as the test runner and **Playwright for Python** for browser automation.

## Test Scope

The automated tests cover (but are not limited to):

* Navigating to the Automation Exercise
* Register new user account
* Login with valid and invalid user accounts
* Search products and validate there existence
* Adding products to the shopping cart
* Opening and validating the cart page
* Basic assertions for page content and behavior

## Tech Stack

* **Python** – Programming language
* **pytest** – Test framework
* **Playwright (Python)** – Browser automation library
* **pytest-playwright** – Pytest plugin for Playwright integration

## Prerequisites

Ensure the following are installed on your system:

* **Python 3.9+**
* **pip** (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/qascenarios/automationexercise-ii.git
cd automationexercise-ii
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\\Scripts\\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

## Running Tests

Run all tests in headless mode:

```bash
pytest
```

Run tests in headed (UI) mode:

```bash
pytest --headed
```

Run tests in a specific browser:

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

Run a specific test file:

```bash
pytest tests/auth/test_register.py
```

## Test Reports and run allure server

Pytest output is shown in the terminal by default.

To generate an Allure report run:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Docker Containerization:

The tests are packaged into a Docker image, making them easy to run on any machine without local setup.

# Run tests using the prebuilt docker image:

```bash
docker pull topdandy/automationexercise-ii:latest
docker run --rm -v $(pwd)/allure-results:/app/allure-results topdandy/automationexercise-ii:latest
```

# Clone the Repository and Run via Script:

```bash
git clone https://github.com/qascenarios/automationexercise-ii.git
cd automationexercise-ii
```

```bash
chmod +x run-tests.sh
./run-tests.sh
```

## Supported Browsers

Using pytest-playwright, tests can run on:

* Chromium
* Firefox
* WebKit

Browser selection is controlled via pytest command-line options.

## Best Practices Followed

* Clear and descriptive test names
* Reusable pytest fixtures
* Independent and repeatable test cases
* Reliable Playwright and bespoke locators
* No hard-coded waits (uses auto-waiting and assertions)

## License

This project is intended for **learning, practice, and demonstration purposes only**.

## Author

Created as a **pytest-playwright E2E testing practice project**.
