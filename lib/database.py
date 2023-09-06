# Import the required modules
from sqlalchemy import create_engine
from models import Base  # Import the Base class that contains your database models

def create_database():
    # Define the database connection URL (SQLite in this example)
    database_url = "sqlite:///expenses_tracker.db"

    # Create an SQLAlchemy engine
    engine = create_engine(database_url)

    # Create the database tables based on the models
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    # Call the create_database function to initialize the database
    create_database()
    print("Database initialized.")
