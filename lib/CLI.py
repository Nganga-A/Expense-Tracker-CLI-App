import click
from sqlalchemy.orm import Session
from database import create_database  # Import your database setup function
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
@expense_tracker.command()
@click.option('--username', prompt='Username', help='User username')
@click.option('--password', prompt='Password', hide_input=True, help='User password')
def create_user(username, password):
    db = Session()  # Create a SQLAlchemy session
    user = UserClassMethods.create_user(db, username, password)
    click.echo(f"User {user.username} created successfully.")


# Command to create a new budget
@expense_tracker.command()
@click.option('--user-id', prompt='User ID', help='User ID')
@click.option('--category-id', prompt='Category ID', help='Category ID')
@click.option('--amount', prompt='Budget Amount', help='Budget Amount')
def create_budget(user_id, category_id, amount):
    db = Session()  # Create a SQLAlchemy session
    budget = BudgetClassMethods.create_budget(db, user_id, category_id, float(amount))
    click.echo(f"Budget entry with ID {budget.id} created successfully.")


# Command to list all budgets for a user
@expense_tracker.command()
@click.option('--user-id', prompt='User ID', help='User ID')
def list_budgets(user_id):
    db = Session()  # Create a SQLAlchemy session
    budgets = BudgetClassMethods.get_budgets_by_user(db, int(user_id))
    
    if budgets:
        click.echo("Budgets for User:")
        for budget in budgets:
            click.echo(f"ID: {budget.id}, Category: {BudgetClassMethods.get_category_name_for_budget(db, budget.id)}, Amount: {budget.amount}")
    else:
        click.echo("No budgets found for the user.")


# Command to create a new expense
@expense_tracker.command()
@click.option('--user-id', prompt='User ID', help='User ID')
@click.option('--category-id', prompt='Category ID', help='Category ID')
@click.option('--date', prompt='Expense Date (YYYY-MM-DD)', help='Expense Date (YYYY-MM-DD)')
@click.option('--description', prompt='Description', help='Expense Description')
@click.option('--amount', prompt='Expense Amount', help='Expense Amount')
def create_expense(user_id, category_id, date, description, amount):
    db = Session()  # Create a SQLAlchemy session
    expense = ExpenseClassMethods.create_expense(db, user_id, category_id, date, description, float(amount))
    click.echo(f"Expense entry with ID {expense.id} created successfully.")


# Command to list all expenses for a user
@expense_tracker.command()
@click.option('--user-id', prompt='User ID', help='User ID')
def list_expenses(user_id):
    db = Session()  # Create a SQLAlchemy session
    expenses = ExpenseClassMethods.get_expenses_by_user(db, int(user_id))
    
    if expenses:
        click.echo("Expenses for User:")
        for expense in expenses:
            click.echo(f"ID: {expense.id}, Category: {ExpenseClassMethods.get_category_name_for_expense(db, expense.id)}, Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}")
    else:
        click.echo("No expenses found for this user.")


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
@click.option('--user-id', prompt='User ID', help='User ID')
def compare_user_budgets_expenses(user_id):
    db = Session()  # Create a SQLAlchemy session

    # Retrieve the user's budgets and expenses
    budgets = BudgetClassMethods.get_budgets_by_user(db, int(user_id))
    expenses = ExpenseClassMethods.get_expenses_by_user(db, int(user_id))

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


# Command to generate a report for a user
@expense_tracker.command()
@click.option('--user-id', prompt='User ID', help='User ID')
def generate_user_report(user_id):
    db = Session()  # Create a SQLAlchemy session

    # Retrieve the user's name
    user = UserClassMethods.get_user_by_id(db, int(user_id))
    user_name = user.username if user else "User Not Found"

    # Retrieve the user's budgets and expenses
    budgets = BudgetClassMethods.get_budgets_by_user(db, int(user_id))
    expenses = ExpenseClassMethods.get_expenses_by_user(db, int(user_id))

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
        click.echo(f"\nCategory: {category}")
        click.echo(f"Total Budgeted Amount: {total_budget}")
        click.echo(f"Total Expenses Amount: {total_expenses}")



if __name__ == '__main__':
    expense_tracker()





































if __name__ == '__main__':
    expense_tracker()
