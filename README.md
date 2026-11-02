# QA Automation Framework

UI test automation for [Sauce Demo](https://www.saucedemo.com) using **Python, pytest and Playwright**, structured with the **Page Object Model**.

## Structure
```
pages/      Page objects (locators + actions per page)
tests/      Test cases, grouped by feature; conftest.py holds fixtures
docs/       TEST_PLAN.md – scope, approach, and test case table
config.py   URLs and test data
```

## Run it
```bash
pip install -r requirements.txt
playwright install chromium
pytest                    # all tests
pytest -m smoke           # smoke only
pytest --headed           # watch the browser
```
An HTML report is written to `reports/report.html`.

## How it works
1. **Page objects** wrap each page's locators and actions, so tests read like user steps and a UI change only needs one fix.
2. **Fixtures** (`conftest.py`) handle setup such as opening the site and logging in.
3. **Markers** (`smoke`, `regression`, `negative`) let you run targeted subsets.
4. **CI**: GitHub Actions runs the suite on every push and uploads the report.

See `docs/TEST_PLAN.md` for the full test plan.
