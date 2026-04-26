from fastapi import APIRouter,Depends
from schemas import InsertCategory,ShowCategory
from db.Gateways.category_gw import SQL_category
from database import dbManager, get_db
router = APIRouter(prefix="/category", tags=["category"])

@router.post('/')
def insert_category(category:InsertCategory,db:dbManager=Depends(get_db)):
    SQLmanager=SQL_category(db)
    return SQLmanager.create_category(category)

@router.get('/',response_model=list[ShowCategory])
def show_category(db:dbManager=Depends(get_db)):
    SQLmanager=SQL_category(db)
    return SQLmanager.show_category()