# Test Plan – Sauce Demo (https://www.saucedemo.com)

## 1. Objective
Validate the core user journeys of the Sauce Demo e-commerce site (login, product browsing, cart, checkout) using automated UI tests.

## 2. Scope
**In scope:** Login, inventory display and sorting, add-to-cart, checkout flow.
**Out of scope:** Performance, security, accessibility, cross-device testing, the `problem_user` / `performance_glitch_user` accounts.

## 3. Approach & Tools
| Item | Choice |
|---|---|
| Language | Python 3 |
| Test runner | pytest |
| Browser automation | Playwright |
| Design pattern | Page Object Model |
| Reporting | pytest-html |
| CI | GitHub Actions |

## 4. Test Environment
Public demo site, Chromium (headless in CI). Test data lives in `config.py`.

## 5. Entry / Exit Criteria
- **Entry:** site reachable, dependencies installed.
- **Exit:** all smoke tests pass; no open failures in regression set without a logged defect.

## 6. Test Cases
| ID | Area | Scenario | Type | Expected Result |
|---|---|---|---|---|
| TC01 | Login | Valid credentials | Smoke | Redirected to inventory page |
| TC02 | Login | Locked-out user | Negative | "locked out" error shown |
| TC03 | Login | Wrong username/password | Negative | "do not match" error shown |
| TC04 | Login | Empty username | Negative | "Username is required" |
| TC05 | Login | Empty password | Negative | "Password is required" |
| TC06 | Inventory | Products page loads | Smoke | Title "Products", 6 items |
| TC07 | Inventory | Sort price low→high | Regression | Prices ascending |
| TC08 | Inventory | Sort price high→low | Regression | Prices descending |
| TC09 | Cart | Add item | Regression | Cart badge shows 1 |
| TC10 | Checkout | End-to-end purchase | Smoke | "Thank you for your order!" |
| TC11 | Checkout | Missing first name | Negative | "First Name is required" |

## 7. Risks
- Third-party demo site may change locators or be unavailable.
- Tests depend on shared public test accounts.

## 8. Deliverables
Test code, HTML report (`reports/report.html`), this plan.
