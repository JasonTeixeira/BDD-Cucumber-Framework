# BDD Cucumber Framework (behave + Playwright + Allure)

A **production-grade** Behavior-Driven Development framework built with:

- **behave** (Gherkin / Given-When-Then)
- **Playwright** (fast, stable browser automation)
- **Allure** (evidence-first reporting: screenshots, traces, attachments)
- **GitHub Actions CI** (repeatable runs + artifacts)

## Why this repo is “real”
This is not a toy skeleton. It includes:
- A complete project layout (config, pages, utils, steps)
- Deterministic waits + stable selectors
- Artifacts on failure (screenshot + page HTML)
- CI pipeline that publishes test artifacts

## Quickstart

### 1) Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install --with-deps chromium
```

### 2) Run the BDD suite
```bash
behave -f allure -o allure-results
```

### 3) View Allure report (optional)
If you have Allure installed:
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Test target
We use a stable public demo app:
- https://www.saucedemo.com/

## Structure
- `features/` – Gherkin feature files
- `features/steps/` – step definitions
- `src/pages/` – page objects
- `src/config/` – environment config
- `src/utils/` – helpers (attachments, waiting)
- `.github/workflows/` – CI pipeline

