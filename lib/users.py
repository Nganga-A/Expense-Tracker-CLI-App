from sqlalchemy.orm import Session
from models import User, Budget, Expense
import bcrypt
from datetime import datetime

#create a user with hashed password
def create_user(db: Session,username:str, password:bytes):
    #hash the password before storing it
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    user = User(username=username, password_hash=password_hash)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#Retrieve a user by their ID.
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

#Retrieve a user by their username.
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

#Retrieve the budgets associated with a user.
def get_user_budgets(db: Session, user_id: int):
    return db.query(Budget).filter(Budget.user_id == user_id).all()

#Create a budget entry for a user.
def create_user_budget(db: Session, user_id: int, category_id: int, amount: float):
    budget = Budget(user_id=user_id, category_id=category_id, amount=amount)
    db.add(budget)
    db.commit()
    db.refresh(budget)
    return budget


#Create an expense entry for a user.
def create_user_expense(db: Session, user_id: int, category_id: int, date: datetime, description: str, amount: float):
    expense = Expense(user_id=user_id, category_id=category_id, date=date, description=description, amount=amount)
    
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

# Retrieve expenses associated with a user.
def get_user_expenses(db: Session, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()





# def login_user(db: Session, username: str, password: str) -> str:
#     """
#     Login a user by verifying their username and password.
#     Returns a message indicating success or failure.
#     """
#     user = db.query(User).filter(User.username == username).first()
#     if user:
#         # Retrieve the stored hashed password from the database
#         stored_password_hash = user.password_hash.encode('utf-8')

#         # Hash the entered password for comparison
#         entered_password = password.encode('utf-8')

#         # Compare the hashed entered password with the stored hashed password
#         if bcrypt.checkpw(entered_password, stored_password_hash):
#             return "Login successful. Welcome, {}!".format(username)
#         else:
#             return "Login failed. Incorrect password."
#     else:
#         return "Login failed. User not found."

