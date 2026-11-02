# 🐞 QA Practice Hub

**End-to-End Test Automation Framework** for the [QA Practice Hub](https://qapracticehub.com) — built with BDD, Playwright & pytest, powered by Allure reports.

---

## 📖 About

**QA Practice Hub** is an automated end-to-end testing project that turns manual QA workflows into executable specs.

The framework combines **Behavior-Driven Development (BDD)** with **Playwright UI automation** and the **pytest** ecosystem to deliver fast, readable, and reliable E2E tests for the web forms of the practice application.

Every scenario is written in **Gherkin** (`.feature` files), mapped to **step definitions**, implemented against **Page Object** models, and executed with **Playwright** as the browser automation engine — with rich reporting via **Allure**.

---

## 🛠 Tech Stack

| Category          | Tools & Technologies                    |
|-------------------|-----------------------------------------|
| **Language**      | Python 3.x                              |
| **UI Automation** | Playwright                              |
| **Test Runner**   | pytest                                  |
| **BDD**           | Gherkin / Cucumber *(via `pytest-bdd`)* |
| **Reporting**     | Allure Report                           |
| **Architecture**  | Page Object Model (POM)                 |

---

## 📁 Project Structure

```
qa_practice_hub/
├── features/               # 📄 Gherkin feature files (.feature)
├── steps/                  # 🧩 BDD step definitions
├── pages/                  # 🧱 Page Object classes
├── reports/                # 📊 Allure HTML reports
├── conftest.py             # ⚙️ Shared fixtures (e.g. screenshot on failure)
├── pytest.ini              # ⚙️ Pytest & BDD configuration (markers)
└── requirements.txt        # 📦 Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [Playwright](https://playwright.dev/python/) browsers installed

### Installation

```bash
pip install -r requirements.txt
playwright install
```

### Run Tests

```bash
# Run full regression suite
pytest

# Run smoke tests only
pytest -m smoke

# Run regression tests only
pytest -m regression
```

### View Allure Report

```bash
allure serve reports/allure_report
```

---

## 🧪 Test Reports & Results

- **Allure** generates detailed HTML reports with steps, logs, screenshots, and environment data.
- A **screenshot on failure** is automatically attached to the Allure report via the shared `conftest.py` fixture.

---

## ✅ Markers

| Marker       | Description                     |
|--------------|---------------------------------|
| `smoke`      | Quick checks for critical flows |
| `regression` | Full regression test suite      |
| `negative`   | Only negative test suite        |

---

## 👨‍💻 Author
Alexandr Gusev — QA Engineer (Manual + Automation)  
Telegram: @xS4nty  
[GitHub](https://github.com/S4NTY) · [LinkedIn ](https://www.linkedin.com/in/alexandr-gusev-2b47431b4/)  
