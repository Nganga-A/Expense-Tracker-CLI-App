#!/usr/bin/env python3


import click
from sqlalchemy.orm import Session

from database import SessionLocal # Import your database setup function
from users import UserClassMethods
from budgets import BudgetClassMethods
from expenses import ExpenseClassMethods
from categories import CategoryClassMethods 




# Create a Click group for your CLI commands
@click.group()
def expense_tracker():
    pass


# Command to initialize the database
@expense_tracker.command()
def initdb():
    create_database()  # Call function to create the database
    click.echo("Expense Tracker database initialized.")


# Command to create a new user
# @expense_tracker.command()
# @click.option('--username', prompt='Username', help='User username')
# @click.option('--password', prompt='Password', hide_input=True, help='User password')
# def create_user(username, password):
#     db = Session()  # Create a SQLAlchemy session
#     user = UserClassMethods.create_user(db, username, password)
#     click.echo(f"User {user.username} created successfully.")
@expense_tracker.command()
def create_user():
    # Establish a database session
    db_session = SessionLocal()

    # Prompt for username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Create a new user
        user = UserClassMethods.create_user(db_session, username, password)

        # Commit the changes to the database
        db_session.commit()

        click.echo(f"User {username} created successfully.")
    except Exception as e:
        click.echo(f"Error creating user: {str(e)}")
    finally:
        # Close the session
        db_session.close()


# Command to create a new budget
@expense_tracker.command()
@click.option('--username', prompt='Username', help='User Username')
@click.option('--category-name', prompt='Category Name', help='Category Name')
@click.option('--amount', prompt='Budget Amount', help='Budget Amount')
def create_budget(username, category_name, amount):
    db = Session()  # Create a SQLAlchemy session
    
    # Retrieve the user by username
    user = UserClassMethods.get_user_by_username(db, username)
    
    if user:
        # Retrieve the category by name or create it if it doesn't exist
        category = CategoryClassMethods.get_category_by_name(db, category_name)
        if not category:
            category = CategoryClassMethods.create_category(db, category_name)

        # Create the budget with the user and category
        budget = BudgetClassMethods.create_budget(db, user.id, category.id, float(amount))
        click.echo(f"Budget entry with name {category_name} created successfully.")
    else:
        click.echo(f"User with username '{username}' not found.")


# Command to list all budgets for a user
@expense_tracker.command()
@click.option('--username', prompt='Username', help='User username')
def list_budgets(username):
    db = Session()  # Create a SQLAlchemy session
    
    # Retrieve the user by username
    user = UserClassMethods.get_user_by_username(db, username)
    
    if user:
        budgets = BudgetClassMethods.get_budgets_by_user(db, user.id)
        
        if budgets:
            click.echo(f"Budgets for User {username}:")
            for budget in budgets:
                category_name = BudgetClassMethods.get_category_name_for_budget(db, budget.id)
                click.echo(f"Category: {category_name}, Amount: {budget.amount}")
        else:
            click.echo(f"No budgets found for User {username}.")
    else:
        click.echo(f"User with username '{username}' not found.")


# Command to create a new expense
@expense_tracker.command()
@click.option('--username', prompt='Username', help='User username')
@click.option('--category-name', prompt='Category Name', help='Category Name')
@click.option('--date', prompt='Expense Date (YYYY-MM-DD)', help='Expense Date (YYYY-MM-DD)')
@click.option('--description', prompt='Description', help='Expense Description')
@click.option('--amount', prompt='Expense Amount', help='Expense Amount')
def create_expense(username, category_name, date, description, amount):
    db = Session()  # Create a SQLAlchemy session
    
    # Retrieve the user by username
    user = UserClassMethods.get_user_by_username(db, username)
    
    if user:
        # Retrieve the category by name or create it if it doesn't exist
        category = CategoryClassMethods.get_category_by_name(db, category_name)
        if not category:
            category = CategoryClassMethods.create_category(db, category_name)

        # Create the expense with the user and category
        expense = ExpenseClassMethods.create_expense(db, user.id, category.id, date, description, float(amount))
        click.echo(f"Expense entry with name {category_name} created successfully.")
    else:
        click.echo(f"User with username '{username}' not found.")


# Command to list all expenses for a user
@expense_tracker.command()
@click.option('--username', prompt='Username', help='User username')
def list_expenses(username):
    db = Session()  # Create a SQLAlchemy session
    
    # Retrieve the user by username
    user = UserClassMethods.get_user_by_username(db, username)
    
    if user:
        expenses = ExpenseClassMethods.get_expenses_by_user(db, user.id)
        
        if expenses:
            click.echo(f"Expenses for User {username}:")
            for expense in expenses:
                category_name = ExpenseClassMethods.get_category_name_for_expense(db, expense.id)
                click.echo(f"Category: {category_name}, Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}")
        else:
            click.echo(f"No expenses found for User {username}.")
    else:
        click.echo(f"User with username '{username}' not found.")


# Command to create a new category
@expense_tracker.command()
@click.option('--name', prompt='Category Name', help='Category Name')
def create_category(name):
    db = Session()  # Create a SQLAlchemy session
    category = CategoryClassMethods.create_category(db, name)
    click.echo(f"Category {category.name} created successfully.")


# Command to list all categories
@expense_tracker.command()
def list_categories():
    db = Session()  # Create a SQLAlchemy session
    categories = CategoryClassMethods.get_all_categories(db)
    
    if categories:
        click.echo("Expense Categories:")
        for category in categories:
            click.echo(f"ID: {category.id}, Name: {category.name}")
    else:
        click.echo("No categories found.")


# Command to compare a user's budgets and expenses for all categories
@expense_tracker.command()
@click.option('--username', prompt='Username', help='User username')
def compare_user_budgets_expenses(username):
    db = Session()  # Create a SQLAlchemy session
    
    # Retrieve the user by username
    user = UserClassMethods.get_user_by_username(db, username)
    
    if user:
        budgets = BudgetClassMethods.get_budgets_by_user(db, user.id)
        expenses = ExpenseClassMethods.get_expenses_by_user(db, user.id)

        # Create a dictionary to store the summary for each category
        category_summary = {}

        # Group budgets by category and calculate the total budgeted amount
        for budget in budgets:
            category_name = BudgetClassMethods.get_category_name_for_budget(db, budget.id)
            if category_name in category_summary:
                category_summary[category_name]["budgets"].append(budget.amount)
            else:
                category_summary[category_name] = {"budgets": [budget.amount], "expenses": []}

        # Group expenses by category and calculate the total expenses amount
        for expense in expenses:
            category_name = ExpenseClassMethods.get_category_name_for_expense(db, expense.id)
            if category_name in category_summary:
                category_summary[category_name]["expenses"].append(expense.amount)
            else:
                category_summary[category_name] = {"budgets": [], "expenses": [expense.amount]}

        # Calculate and display the summary for each category
        for category, data in category_summary.items():
            total_budget = sum(data["budgets"])
            total_expenses = sum(data["expenses"])
            difference = total_budget - total_expenses

            click.echo(f"Category: {category}")
            click.echo(f"Total Budgeted Amount: {total_budget}")
            click.echo(f"Total Expenses Amount: {total_expenses}")
            click.echo(f"Difference/Savings (Budget - Expenses): {difference}")
            click.echo("-------------------------------------------------------")
    else:
        click.echo(f"User with username '{username}' not found.")


# Command to generate a report for a user
@expense_tracker.command()
@click.option('--username', prompt='Username', help='User username')
def generate_user_report(username):
    db = Session()  # Create a SQLAlchemy session
    
    # Retrieve the user by username
    user = UserClassMethods.get_user_by_username(db, username)
    
    if user:
        # Retrieve the user's name
        user_name = user.username

        budgets = BudgetClassMethods.get_budgets_by_user(db, user.id)
        expenses = ExpenseClassMethods.get_expenses_by_user(db, user.id)

        # Create a set to store unique category names
        category_names = set()

        # Create a dictionary to group budgets and expenses by category
        budget_expense_summary = {}

        # Group budgets by category
        for budget in budgets:
            category_name = BudgetClassMethods.get_category_name_for_budget(db, budget.id)
            category_names.add(category_name)
            if category_name in budget_expense_summary:
                budget_expense_summary[category_name]["budgets"].append(budget.amount)
            else:
                budget_expense_summary[category_name] = {"budgets": [budget.amount], "expenses": []}

        # Group expenses by category
        for expense in expenses:
            category_name = ExpenseClassMethods.get_category_name_for_expense(db, expense.id)
            category_names.add(category_name)
            if category_name in budget_expense_summary:
                budget_expense_summary[category_name]["expenses"].append(expense.amount)
            else:
                budget_expense_summary[category_name] = {"budgets": [], "expenses": [expense.amount]}

        # Display the user's name
        click.echo(f"User Name: {user_name}")

        # Display the list of categories
        click.echo("Categories:")
        for category_name in category_names:
            click.echo(f"- {category_name}")

        # Display the report for each category
        for category, data in budget_expense_summary.items():
            total_budget = sum(data["budgets"])
            total_expenses = sum(data["expenses"])
            difference = total_budget - total_expenses

            click.echo(f"\nCategory: {category}")
            click.echo(f"Total Budgeted Amount: {total_budget}")
            click.echo(f"Total Expenses Amount: {total_expenses}")
            click.echo(f"Difference/Savings (Budget - Expenses): {difference}")
    else:
        click.echo(f"User with username '{username}' not found.")


if __name__ == '__main__':
    expense_tracker()




if __name__ == '__main__':
    expense_tracker()
