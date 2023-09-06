from sqlalchemy.orm import Session
from models import Expense
from datetime import datetime
from categories import get_category_by_name

class ExpenseClassMethods:
    @classmethod
    def create_expense(
        cls,
        db: Session,
        user_id: int,
        category_id: int,
        date: datetime,
        description: str,
        amount: float,
    ):
        """
        Create an expense entry.
        """
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

    @classmethod
    def get_expense_by_id(cls, db: Session, expense_id: int):
        """
        Retrieve an expense entry by its ID.
        """
        return db.query(Expense).filter(Expense.id == expense_id).first()

    @classmethod
    def get_expenses_by_user(cls, db: Session, user_id: int):
        """
        Retrieve expenses associated with a specific user.
        """
        return db.query(Expense).filter(Expense.user_id == user_id).all()

    @classmethod
    def delete_expense(cls, db: Session, expense_id: int):
        """
        Delete an expense entry by its ID.
        Returns a message indicating success or failure.
        """
        expense = db.query(Expense).filter(Expense.id == expense_id).first()

        if expense:
            db.delete(expense)
            db.commit()
            return "Expense deleted successfully"
        else:
            return "Expense not found. Deletion failed."

    @classmethod
    def get_category_name_for_expense(cls, db: Session, expense_id: int):
        """
        Retrieve the name of the category associated with an expense by its ID.
        Returns None if the expense or category is not found.
        """
        expense = db.query(Expense).filter(Expense.id == expense_id).first()
        
        if expense:
            category = get_category_by_name(db, expense.category.name)
            return category.name if category else None
        else:
            return None
