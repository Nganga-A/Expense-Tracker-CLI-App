from sqlalchemy.orm import Session
from models import Expense
from datetime import datetime
from categories import get_category_by_name

#Create an expense entry.
def create_expense(
    db: Session,
    user_id: int,
    category_id: int,
    date: datetime,
    description: str,
    amount: float,
):
    expense = Expense(
        user_id=user_id,
        category_id=category_id,
        date=date,
        description=description,
        amount=amount
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

#retrieve expense by its ID
def get_expense_by_id(db:Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()

#Retrieve expenses associated with a specific user.
def get_expenses_by_user(db:Session, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()

#Delete an expense by its ID
def delete_expense(db:Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if expense:
        db.delete(expense)
        db.commit()
        return "Expense deleted successfully"
    else:
        return "Expense not found. Deletion failed."
    

# #Retrieve the name of the category associated with an expense by its ID.
# def get_category_name_for_expense(db: Session, expense_id: int):
#     """
#     Retrieve the name of the category associated with an expense by its ID.
#     Returns None if the expense or category is not found.
#     """
#     expense = db.query(Expense).filter(Expense.id == expense_id).first()
    
#     if expense:
#         category = get_category_by_name(db, expense.category.name)
#         return category.name if category else None
#     else:
#         return None