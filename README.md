# Python Test Automation Framework

![Python Tests](https://github.com/krzysiuuus/python-test-automation-framework/actions/workflows/python-tests.yml/badge.svg)

Automated UI testing project created with Python, Selenium WebDriver and Pytest.

The project is based on the Page Object Pattern and contains automated end-to-end tests for web application scenarios such as flight search, hotel search and booking flows.

## Technologies

- Pythondawaj na spotkani
- Selenium WebDriver
- Pytest
- Page Object Pattern
- Allure Reports
- GitHub Actions

## Features

- Page Object Pattern architecture
- End-to-end UI automation
- GitHub Actions CI pipelineŚ
- Allure reporting
- Headless browser execution
- Test data management
- Screenshot attachment on test failure

## Architecture

The framework is based on the Page Object Pattern design approach:

- locators separated from test logic
- reusable page classes
- centralized test configuration
- pytest fixtures for driver management
- Allure integration for reporting
- GitHub Actions CI integration

## API Testing

The framework also contains API automated tests built with:

- Requests
- Pytest
- Allure Reports

Implemented API features:

- GET requests
- POST requests
- PUT requests
- DELETE requests
- Positive and negative scenarios
- JSON schema validation
- Response time assertions
- Bearer token authentication
- Reusable API client abstraction
- Parametrized API tests

API tests are separated from UI tests and executed in a dedicated GitHub Actions pipeline job.

## Project Structure

```text
python-ui-test-framework/
├── api_tests/
│   ├── data/
│   ├── schemas/
│   ├── tests/
│   └── utils/
├── page_object_pattern/
│   ├── locators/
│   ├── pages/
│   └── tests/
├── reports/
├── screenshots/
├── requirements.txt
├── pytest.ini
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/krzysiuuus/python-ui-test-framework.git
cd python-ui-test-framework
```

Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest
```

Run selected test file:

```bash
pytest page_object_pattern/tests/test_flight_search.py
```

## Allure Report

Run tests with Allure results:

```bash
pytest --alluredir=reports
```

Generate and open report:

```bash
allure serve reports
```

## CI/CD

The project uses GitHub Actions for Continuous Integration.

Pipeline automatically:

- installs dependencies
- runs automated tests
- generates test reports
- validates project integrity on every push

## Screenshots

### GitHub Actions CI

![GitHub Actions](screenshots/github-actions.png)

### Allure Report

![Allure Report](screenshots/allure-report.png)

## Future Improvements

- Docker support
- Parallel execution
- Test retries
- Cross-browser testing
- Performance testing

## Author

Created by [krzysiuuus](https://github.com/krzysiuuus)
