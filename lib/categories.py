from sqlalchemy.orm import Session
from models import Category

class CategoryClassMethods:
    @classmethod  #Create a new category
    def create_category(cls, db: Session, name: str, user_id:int):
        category = Category(name=name, user_id = user_id)

        db.add(category)
        db.commit()
        db.refresh(category)
        return category


    @classmethod  #Retrieve a category by its ID.
    def get_category_by_id(cls, db: Session, category_id: int):
        return db.query(Category).filter(Category.id == category_id).first()


    @classmethod  #Retrieve a category by its name
    def get_category_by_name(cls, db: Session, name):
        return db.query(Category).filter(Category.name == name).first()


    @classmethod  #Retrieve all expense categories associated by user
    def get_all_categories_by_user(cls, db: Session, user_id: int):
        return db.query(Category).filter(Category.user_id == user_id).all()


    @classmethod  #Delete a category 
    def delete_category(cls, db: Session, category_id: int):
        category = db.query(Category).filter(Category.id == category_id).first()

        if category:
            db.delete(category)
            db.commit()
            return f"Category {category.name} deleted successfully."
        else:
            return f"Category not found. Deletion failed."
