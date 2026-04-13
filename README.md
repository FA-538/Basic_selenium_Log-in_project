# Selenium Automation Framework 🚀

This project demonstrates a step-by-step development of a Selenium-based automation testing framework using Python and pytest.

The goal of this project is to showcase how a basic automation script evolves into a structured, scalable, and maintainable test framework.

---

## 🧠 Project Evolution

This framework was built incrementally to demonstrate learning progression:

### Step 1: Basic Selenium Script
- Created a simple login and logout automation script
- Used Selenium WebDriver
- Applied implicit and explicit waits

### Step 2: Structured Testing with unittest
- Converted script into a structured test using `unittest`
- Implemented setup and teardown methods

### Step 3: Migration to pytest
- Replaced unittest with pytest
- Introduced fixtures using `conftest.py`
- Simplified test execution and structure

### Step 4: Page Object Model (POM)
- Separated UI interactions into page classes
- Created:
  - `LoginPage` (handles login actions)
  - `HomePage` (handles logout actions)

### Step 5: Locator Separation
- Moved all locators into dedicated locator classes
- Improved maintainability and readability

### Step 6: Dependency Management
- Added `requirements.txt` for easy setup

### Step 7: HTML Reporting
- Integrated `pytest-html` for generating test reports

---

## 📁 Project Structure
