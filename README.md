# Autotests.-Final-task
Autotests with Selenium, Python and Pytest. Page Object Model is used.

Python 3.7.6
Pytest 5.1.1
Selenium 3.14.0

Command for install pakages to environment:
pip install -r \path\requirements.txt

Command for run review tests:
pytest -v --tb=line --language=en -m need_review

Files:

Pages:
base_page.py: base page;
basket_page.py: basket page;
links.py: links for pages;
locators.py: locators for elements on pages;
login_page.py: login page;
main_page.py: main page;
product_page.py: product page.

Other files:
__init__.py;
conftest.py: fixture for function: choose browser and language;
pytest.ini: markers for tests;
README.md: project description;
requirenemts.txt: requirements for environment;
test_main_page: main page tests;
test_product_page: product page tests.


