# Expense-Tracker-CLI-App
The Expense Tracker CLI Application is designed to help individuals track their expenses, manage budgets, and gain insights into their spending habits by expense analysis. It provides a command-line interface for users to interact with the application.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Folder Structure](#Project-Folder-Structure)
- [Usage](#usage)
  - [Creating a User](#creating-a-user)
  - [Creating a Budget](#creating-a-budget)
  - [Listing Budgets](#listing-budgets)
  - [Creating an Expense](#creating-an-expense)
  - [Listing Expenses](#listing-expenses)
  - [Creating a Category](#creating-a-category)
  - [Listing Categories](#listing-categories)
  - [Comparing Budgets and Expenses](#comparing-budgets-and-expenses)
  - [Generating User Reports](#generating-user-reports)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will guide you on setting up and using the Expense Tracker CLI application.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python3 v3.10 +

- SQLAlchemy v2.0.20

- Alembic v1.12.0

- click

Virtual environment (optional but recommended)

### Installation

1. Clone the repository:
   ```sh
   git clone git@github.com:Nganga-A/Expense-Tracker-CLI-App.git

### Packages

- alembic: 1.8.1
- importlib-metadata: 6.0.0
- importlib-resources: 5.10.0
- SQLAlchemy: 1.4.41

### Requires

- Python Version: 3.10.12

## Project Setup

### 1. Clone the repository

```

git clone git@github.com:Nganga-A/Expense-Tracker-CLI-App.git

```

### 2. Navigate to the project directory

```

cd Expense-Tracker-CLI-App

```

### 3. Install required dependencies

In the project directory, install the required dependencies

```
pipenv install

```

### 4. Enter the virtual enviroment

```
pipenv shell

```


## Project Folder Structure

```
expense_tracker/
│
├── expense_tracker/
│   ├── __init__.py
│   ├── main.py       # Your main application code
│   ├── models.py     # SQLAlchemy model definitions
│   ├── users.py      # User-related methods
│   ├── budgets.py    # Budget-related methods
│   ├── expenses.py   # Expense-related methods
│   └── categories.py # Category-related methods
|   └── expense_tracker.db #database
|   └── database.py    #Connection to database
│
└── cli/
    ├── __init__.py
    └── app.py         # Your CLI code (Click or Fire)

```


## Usage
1. Configure the application settings and database connection.
2. Initialize the database and create necessary tables.
3. Run the application using the command-line interface (CLI).


## Contributions

Contributions are welcome! Please open an issue or pull request for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Created by [Abed Nganga Njuguna ](https://github.com/Nganga-A)