from sqlalchemy.orm import Session
from models import Category


#Create a new category
def create_category(db: Session, name:str):
    category = Category(name=name)

    db.add(category)
    db.commit()
    db.refresh(category)
    return category

#Retrieve a category by its ID.
def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

#Retrieve a category by its name.
def get_category_by_name(db: Session, name):
    return db.query(Category).filter(Category.name == name).first()

#Retrieve all expense categories.
def get_all_categories(db: Session):
    return db.query(Category).all()

#Delete a category
def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if category:
        db.delete(category)
        db.commit()
        return "Category {category} deleted successfully."
    else:
        return "Category {category} not found. Deletion Failed."

