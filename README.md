# FinTracker

* FinTracker is an open-source web application to help you take control of your personal finances.  Track your income, expenses, budgets, and investments with this flexible and customizable tool. 
* This repository manages the backend codebase for the project.

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

4. **Configure Database (See [Connecting to database](#connecting-to-mysql-database)) :**
    * Create a MySQL database named `fintracker`.
    * Update the database connection details in an environment file or configuration mechanism of your choice.

5. **Run the Backend Development Server:**
   * Run the main.py file.
6. Results:
   * In your browser go to `http://localhost:8000/`.
   * To see Swagger docs, go to `http://localhost:8000/docs`.

## Connecting to MySQL Database
1. Download MySQL: [MySQL Installer](https://dev.mysql.com/downloads/installer/).
2. Follow on screen instructions to install MySQL.
3. Open MySQL workbench.
4. Create a database in your local instance of MySQL using workbench:
   ```sql
   CREATE DATABASE fintracker_dev;
   ```
   Here, we have created a database called `fintracker_dev`.
5. Create the `.env` file in the root directory of the project `fin-tracker-backend`.
   * Include following variable in the .env file,
     ```.env
     SQLALCHEMY_DATABASE_URL_DEV="mysql+pymysql://<username>:<password>@localhost:3306/fintracker_dev"
     ```
   * Here, replace `<username>` and `<password>` with actual values for the database connection.
   * Please remember to change the `PORT` (3306) in the above connection link if you use a different port.
6. Now you have successfully set up the database connection. Run `main.py` to check whether it works.


## Contributing

We welcome contributions to FinTracker! Please see our contributing guidelines in `CONTRIBUTING.md` for details on how to submit issues, propose changes, and submit pull requests.

## Community
Discord: [Join the Discord Server](https://discord.gg/PDnbF5Qb)

## License
This project is licensed under the [MIT License](LICENSE.md).
