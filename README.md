# Expense-Tracker-CLI-App
The Expense Tracker CLI Application is designed to help individuals track their expenses, manage budgets, and gain insights into their spending habits by expense analysis. It provides a command-line interface for users to interact with the application.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Folder Structure](#Project-Folder-Structure)
- [Usage](#usage)
  - [Creating a User](#creating-a-user)
  - [Listing Users](#listing-users)
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
    └── CLI.py          # CLI code

```


## Usage
1. Configure the application settings and database connection.
2. Initialize the database and create necessary tables.
3. Run the application using the command-line interface (CLI).

### Creating a User

Use Command `create-user`
```sh
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ create-user
Username: John Doe
Password: 123
User John Doe created successfully.

```

### Listing Users

Use Command `list-users`

```sh
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ list-users
List of Users:
Username: asdfgh
Username: Abed N
Username: Abbys 456
Username: Collins
Username: Joy
Username: Dennis
Username: Pauline
Username: dfgh
Username: Pauline 

```

### Creating a Budget

Use Command `create-budget`

```sh



```

### Listing Budgets

Use Command `list-budgets`

```sh
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ list-budgets
Username: Joy
Budgets for User Joy:
Category: Food, Amount: 4000.0
Category: Medicine, Amount: 4000.0
Category: Drinks, Amount: 4000.0

```

### Creating an Expense

Use Command `create-expense`

```sh


```

### Listing Expenses

Use Command `list-expenses`

```sh

user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ list-expenses
Username: Joy
Expenses for User Joy:
Category: Drinks, Date: 2012-12-12, Description: Konyagi, Amount: 5000.0

```

### Creating a Category

Use Command `create-category`

```sh



```


### Listing Categories

Use Command `list-categories`

```sh


```

### Comparing Budgets and Expenses

Use Command `compare-user-budgets-expenses`

```sh
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ compare-user-budgets-expenses
Username: Pauline
Category: Food
Total Budgeted Amount: 10000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 10000.0
-------------------------------------------------------
Category: Transport
Total Budgeted Amount: 4500.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 4500.0
-------------------------------------------------------
Category: Entertainment
Total Budgeted Amount: 7000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 7000.0
-------------------------------------------------------
Category: Family
Total Budgeted Amount: 7000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 7000.0
-------------------------------------------------------
Category: Sports
Total Budgeted Amount: 5000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 5000.0
-------------------------------------------------------
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ compare-user-budgets-expenses
Username: Quik
Category: Food
Total Budgeted Amount: 70000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 70000.0
-------------------------------------------------------
Category: Dowry
Total Budgeted Amount: 40000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 40000.0
-------------------------------------------------------
Category: Sneakers
Total Budgeted Amount: 10000.0
Total Expenses Amount: 4000.0
Difference/Savings (Budget - Expenses): 6000.0
-------------------------------------------------------
Category: Clothes
Total Budgeted Amount: 10000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 10000.0
-------------------------------------------------------
Category: Meds
Total Budgeted Amount: 0
Total Expenses Amount: 4000.0
Difference/Savings (Budget - Expenses): -4000.0
-------------------------------------------------------

```

```sh
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ compare-user-budgets-expenses
Username: Joy
Category: Food
Total Budgeted Amount: 4000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 4000.0
-------------------------------------------------------
Category: Medicine
Total Budgeted Amount: 4000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 4000.0
-------------------------------------------------------
Category: Drinks
Total Budgeted Amount: 4000.0
Total Expenses Amount: 5000.0
Difference/Savings (Budget - Expenses): -1000.0
-------------------------------------------------------
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ compare-user-budgets-expenses
Username: Pauline
Category: Food
Total Budgeted Amount: 10000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 10000.0
-------------------------------------------------------
Category: Transport
Total Budgeted Amount: 4500.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 4500.0
-------------------------------------------------------
Category: Entertainment
Total Budgeted Amount: 7000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 7000.0
-------------------------------------------------------
Category: Family
Total Budgeted Amount: 7000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 7000.0
-------------------------------------------------------
Category: Sports
Total Budgeted Amount: 5000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 5000.0
-------------------------------------------------------
user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ compare-user-budgets-expenses
Username: Quik
Category: Food
Total Budgeted Amount: 70000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 70000.0
-------------------------------------------------------
Category: Dowry
Total Budgeted Amount: 40000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 40000.0
-------------------------------------------------------
Category: Sneakers
Total Budgeted Amount: 10000.0
Total Expenses Amount: 4000.0
Difference/Savings (Budget - Expenses): 6000.0
-------------------------------------------------------
Category: Clothes
Total Budgeted Amount: 10000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 10000.0
-------------------------------------------------------
Category: Meds
Total Budgeted Amount: 0
Total Expenses Amount: 4000.0
Difference/Savings (Budget - Expenses): -4000.0
-------------------------------------------------------

```

### Generating User Reports

Use Command `generate-user-report`

```sh

user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ generate-user-report
Username: Pauline
User Name: Pauline
Categories:
- Transport
- Entertainment
- Sports
- Food
- Family

Category: Food
Total Budgeted Amount: 10000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 10000.0

Category: Transport
Total Budgeted Amount: 4500.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 4500.0

Category: Entertainment
Total Budgeted Amount: 7000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 7000.0

Category: Family
Total Budgeted Amount: 7000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 7000.0

Category: Sports
Total Budgeted Amount: 5000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 5000.0

```
```sh

user@user-HP-ProBook-450-G5:~/Development/code/Extra/Expense-Tracker-CLI-App/lib$ generate-user-report
Username: Joy
User Name: Joy
Categories:
- Drinks
- Food
- Medicine

Category: Food
Total Budgeted Amount: 4000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 4000.0

Category: Medicine
Total Budgeted Amount: 4000.0
Total Expenses Amount: 0
Difference/Savings (Budget - Expenses): 4000.0

Category: Drinks
Total Budgeted Amount: 4000.0
Total Expenses Amount: 5000.0
Difference/Savings (Budget - Expenses): -1000.0

```

## Contributions

Contributions are welcome! Please open an issue or pull request for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Created by [Abed Nganga Njuguna ](https://github.com/Nganga-A)