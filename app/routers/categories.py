from fastapi import APIRouter,Depends
from db.models import Category, InsertCategory, ReadCategory
from db.Gateways.category_gw import SQL_category
from database import get_session
from sqlmodel import Session
router = APIRouter(prefix="/category", tags=["category"])

@router.post('/')
def insert_category(category:InsertCategory,db:Session=Depends(get_session)):
    SQLmanager=SQL_category(db)
    return SQLmanager.create_category(category)

@router.get('/',response_model=list[ReadCategory])
def show_category(db:Session=Depends(get_session)):
    SQLmanager=SQL_category(db)
    return SQLmanager.show_categories()