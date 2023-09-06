from sqlalchemy.orm import Session
from models import Budget
from categories import get_category_by_name


class BudgetClassMethods:
    @classmethod #Create a budget entry.
    def create_budget(cls, db: Session, user_id: int, category_id: int, amount: float):
        budget = Budget(
            user_id=user_id,
            category_id=category_id,
            amount=amount,
        )
        
        db.add(budget)
        db.commit()
        db.refresh(budget)
        return budget


    @classmethod   #Retrieve a budget entry by its ID.
    def get_budget_by_id(cls, db: Session, budget_id: int):
        return db.query(Budget).filter(Budget.id == budget_id).first()


    @classmethod #Retrieve budgets associated with a specific user.
    def get_budgets_by_user(cls, db: Session, user_id: int):
        return db.query(Budget).filter(Budget.user_id == user_id).all()


    @classmethod  #Delete a budget entry
    def delete_budget(cls, db: Session, budget_id: int):
        budget = db.query(Budget).filter(Budget.id == budget_id).first()
        
        if budget:
            db.delete(budget)
            db.commit()
            return "Budget entry deleted successfully."
        else:
            return "Budget entry not found. Deletion failed."


    @classmethod   #Retrieve the name of the category associated with a budget
    def get_category_name_for_budget(cls, db: Session, budget_id: int):
        """
        Retrieve the name of the category associated with a budget by its ID.
        Returns None if the budget or category is not found.
        """
        budget = db.query(Budget).filter(Budget.id == budget_id).first()
        
        if budget:
            category = get_category_by_name(db, budget.category.name)
            return category.name if category else None
        else:
            return None


    @classmethod #Update the budget value of a certain category.
    def update_budget_value(cls, db: Session, budget_id: int, new_amount: float):
        budget = db.query(Budget).filter(Budget.id == budget_id).first()

        if budget:
            # Update the budget value with the new amount
            budget.amount = new_amount
            db.commit()
            return "Budget value updated successfully."
        else:
            return "Budget entry not found. Update failed."






