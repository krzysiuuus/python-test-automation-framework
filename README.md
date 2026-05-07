# Python UI Test Framework

Automated UI testing project created with Python, Selenium WebDriver and Pytest.

The project is based on the Page Object Pattern and contains automated end-to-end tests for web application scenarios such as flight search, hotel search and booking flows.

## Technologies

- Python
- Selenium WebDriver
- Pytest
- Page Object Pattern
- Allure Reports

## Project Structure

```text
python-ui-test-framework/
├── page_object_pattern/
│   ├── locators/
│   ├── pages/
│   ├── reports/
│   └── tests/
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
pytest --alluredir=page_object_pattern/reports
```

Generate and open report:

```bash
allure serve page_object_pattern/reports
```

## Author

Created by [krzysiuuus](https://github.com/krzysiuuus)
