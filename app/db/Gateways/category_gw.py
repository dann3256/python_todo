from sqlmodel import Session, select
from db.models import Category, InsertCategory, ReadCategory
import uuid

class SQL_category:

    def __init__(self, session: Session):
        self.session = session

    # カテゴリを追加する
    def create_category(self, category: InsertCategory) :
        db_category = Category.model_validate(category)
        self.session.add(db_category)
        self.session.commit()
        self.session.refresh(db_category)
        return None

    # カテゴリを全件取得する
    def show_categories(self) -> list[ReadCategory]:
        statement = select(Category)
        rows = self.session.exec(statement).all()
        return rows