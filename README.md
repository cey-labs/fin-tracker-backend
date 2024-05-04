# FinTracker

* FinTracker is an open-source web application to help you take control of your personal finances.  Track your income, expenses, budgets, and investments with this flexible and customizable tool. 
* This repository manages the codebase for the backend of the project.

## Features
Following features are expected to develop in the future:
* **Account Tracking:** Manage multiple checking, savings, and credit card accounts.
* **Transaction Categorization:** Categorize transactions for detailed spending analysis.
* **Budgeting:** Create budgets and track your progress towards them.
* **Insightful Reports:** Visualize your financial data.

## Project Structure

* `app/`
    * `main.py` - Core FastAPI application.
    * `models/`- Pydantic data models (e.g. User, Account, Transaction).
    * `routers/` - API endpoint definitions (e.g. accounts.py for account-related endpoints).
    * `dependencies/` - Dependency providers (database connection, authentication, etc).
    * `services/` - Business logic (functions for users, accounts, transactions, etc).
* `tests/` - Unit and integration tests.

## Setup Instructions

**Prerequisites**

* Python 3.7+
* MySQL database

**Steps**

1. **Fork this Repository to Your GitHub (Specially, if you're willing to contribute)**

2. **Clone the Repository (to run locally):**
   ```bash
   git clone https://github.com/yourusername/FinTracker.git
   ```

3. **Install Python Dependencies:**
   ```bash
   cd FinTracker
   pip install -r requirements.txt
   ```

4. **Configure Database (Not configured yet. You can omit this step):**
    * Create a MySQL database named `fintracker`.
    * Update the database connection details in an environment file or configuration mechanism of your choice.

5. **Run the Backend Development Server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   or just run the main.py file.
6. Results:
  * In your browser go to `http://localhost:8000/`!
  * To see Swagger docs, go to `http://localhost:8000/docs`

## Connecting to Your MySQL Database (To be Configured)

 `TODO: Configure & document database connection`

## Contributing

We welcome contributions to FinTracker! Please see our contributing guidelines in `CONTRIBUTING.md` for details on how to submit issues, propose changes, and submit pull requests.

## Community
* Discord: [Join the Discord Server](https://discord.gg/PDnbF5Qb)

## License

`MIT LICENSE`
