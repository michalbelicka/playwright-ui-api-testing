# Playwright UI Testing

UI test automation project built with **Python, Playwright and pytest**.

The project focuses on automated testing of the [Automation Exercise](https://www.automationexercise.com/) e-commerce website and demonstrates practical use of **Page Object Model (POM)**, pytest fixtures, reusable test methods and automated test execution with **GitHub Actions**.

## Tech Stack

- Python
- Playwright
- pytest
- Page Object Model (POM)
- GitHub Actions
- Git / GitHub

## Test Coverage

The current UI test suite covers:

- User registration and account deletion
- Valid and invalid login
- Logout
- Adding and removing products from the cart
- Product quantity
- Product search
- Product details
- Checkout and order confirmation

## Project Structure

```text
playwright-ui-testing/
│
├── pages/
│   ├── cart_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── product_details_page.py
│   └── signup_page.py
│
├── tests/
│   └── UI/
│       ├── test_signup_and_delete_account.py
│       ├── test_valid_login.py
│       ├── test_invalid_login.py
│       ├── test_logout.py
│       ├── test_add_product_to_cart.py
│       ├── test_remove_product_from_cart.py
│       ├── test_search_product.py
│       ├── test_product_details.py
│       └── test_quantity.py
│
├── conftest.py
├── requirements.txt
├── TEST_PLAN.md
└── README.md
```

## Test Design

The project uses the **Page Object Model (POM)** to separate test logic from page-specific interactions.

Reusable pytest fixtures are used to prepare common test states, such as:

- Opening the website and handling the cookie banner
- Logging in
- Starting with an empty shopping cart

This keeps the test cases focused on the behavior being verified while reducing duplicated setup code.

## CI/CD

Tests are integrated with **GitHub Actions** and are automatically executed:

- On every push
- On pull requests
- On a scheduled daily run

The workflow:

1. Sets up Python
2. Installs project dependencies
3. Installs Playwright browsers
4. Runs code quality checks
5. Executes the automated test suite

## Future Improvements

- Add API test coverage using Playwright APIRequestContext
- Expand UI test coverage
- Add more advanced test scenarios

## How to Run

Clone the repository:

```bash
git clone https://github.com/michalbelicka/playwright-ui-testing.git
cd playwright-ui-testing
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
pytest
```
