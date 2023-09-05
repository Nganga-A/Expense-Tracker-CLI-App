#Lets define the SQLAlchemy models
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Float
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
    # Other user fields

    # Establish one-to-many relationship with Expense
    expenses = relationship("Expense", back_populates="owner")



class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    # Other category fields

    # Establish one-to-many relationship with Expense
    expenses = relationship("Expense", back_populates="category")



class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    description = Column(String)
    amount = Column(Float)
    
    # Foreign keys to establish relationships
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Define relationships
    owner = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")



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