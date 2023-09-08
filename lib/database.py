# Import the required modules
from sqlalchemy import create_engine
from models import Base  # Import the Base class that contains your database models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection URL (SQLite in this example)
database_url = "sqlite:///expenses_tracker.db"

# Create an SQLAlchemy engine
engine = create_engine(database_url)

# Create the database tables based on the models
Base.metadata.create_all(engine)

# Create a SessionLocal instance for use in your application
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

db = SessionLocal()


# db.bind = engine