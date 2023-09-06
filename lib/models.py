#Lets define the SQLAlchemy models
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Float, Date
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# base class for declarative models
Base = declarative_base()
engine = create_engine('sqlite:///expenses_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    # Establish one-to-many relationship with Expense
    expenses = relationship("Expense", back_populates="owner")
    
    def __init__(self,username : str) :
        self.username = username

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"



class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    # Establish one-to-many relationship with Expense
    expenses = relationship("Expense", back_populates="category")

    def __init__(self,name:str):
        self.name = name

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    description = Column(String)
    amount = Column(Float)
    
    # Foreign keys to establish relationships
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    # relationships
    owner = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")

    def __init__(self, date:date, description:str, amount:float)
        self.date = date
        self.description = description
        self.amount = amount
    
    def __repr__(self):
        return f"<Expense(id={self.id}, date={self.date}, description={self.description}, amount={self.amount})>"


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    amount = Column(Float)

    # Foreign key to establish the relationship with Category
    user_id = Column(Integer, ForeignKey("users.id"))

    # Define relationships
    category = relationship("Category")
    owner = relationship("User")

    def __init__(self,category_id: int, amount:float):
        self.category_id = category_id
        self.amount = amount

    def __repr__(self):
        return f"<Budget(id={self.id}, category_id={self.category_id}, amount={self.amount})>" 