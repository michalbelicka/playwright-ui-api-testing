# Playwright UI & API Testing

UI & API test automation project built with **Python, Playwright and pytest**.

The project focuses on automated testing of the [Automation Exercise](https://www.automationexercise.com/) e-commerce website and demonstrates practical use of **Page Object Model (POM)**, pytest fixtures, parametrization, hooks, reusable test methods and automated test execution with **GitHub Actions**.

## Tech Stack

- Python
- Playwright
- pytest (fixtures, parametrization, hooks)
- Page Object Model (POM)
- GitHub Actions CI pipeline
- Git / GitHub

## Test Coverage

### UI Tests

The current UI test suite covers:

- User registration and account deletion
- Valid and invalid login
- Logout
- Adding and removing products from the cart
- Product quantity
- Product search
- Product details
- Checkout and order confirmation
- Payment workflow
- Invoice download and content verification

### API Tests

The API test suite uses Playwright's APIRequestContext and covers:

- Retrieving all products
- Retrieving all brands
- Searching for products
- Handling requests with missing parameters
- Retrieving user account details by email
- Verifying login credentials
- Creating user accounts
- Updating user account details
- Deleting user accounts
- Verifying HTTP status codes and API response codes
- Validating response messages, JSON structure, field names and data types

## Project Structure

```text
playwright-ui-api-testing/
│
├── pages/
│   ├── cart_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── product_details_page.py
│   |── signup_page.py
│   ├── checkout_page.py
|   └── payment_page.py
|
├── tests/
│   |── UI/
│   |
|   └── API/
|
|── pytest.ini
|── .gitignore
├── conftest.py
├── requirements.txt
├── TEST_PLAN.md
└── README.md
```

## Test Design

The project uses the Page Object Model (POM) to separate UI test logic from page-specific interactions.

Reusable pytest fixtures are used to prepare common test states, such as:

- Opening the website and handling the cookie banner
- Logging in
- Starting with an empty shopping cart
- Creating test user accounts and cleaning them up after API tests

UI tests focus on user interactions and expected application behavior, while API tests verify endpoint responses, status codes, response data and data types.

This approach promotes code reusability, reduces duplicated setup code and keeps test cases focused on the behavior being verified.

## CI/CD

The project uses GitHub Actions to automatically run UI and API tests:

- On every push
- On pull requests
- On a scheduled daily run

The workflow:

1. Sets up Python and installs project dependencies
2. Installs the required Playwright browsers
3. Runs code quality checks
4. Executes the automated test suite
5. Generates an HTML test report
6. Captures screenshots when UI tests fail
7. Uploads the HTML report and failure screenshots as downloadable workflow artifacts

This helps verify that tests continue to pass after code changes and makes it easier to investigate test failures.

## Future Improvements

- Expand API test coverage
- Expand UI test coverage
- Add more advanced test scenarios
- Explore AI-assisted and agentic testing approaches

## How to Run

Clone the repository:

```bash
git clone https://github.com/michalbelicka/playwright-ui-api-testing.git
cd playwright-ui-api-testing
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run the tests:

```bash
pytest -v
```
