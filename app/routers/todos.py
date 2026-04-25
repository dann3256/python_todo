from fastapi import APIRouter,Depends
from schemas import InsertTodo,ShowTodo,UpdateTodo,DeleteTodo
from models import SQL
from database import dbManager, get_db
# URLの先頭の名前を統一／APIをグループ化するためにタグ付け
router = APIRouter(prefix="/todos", tags=["todos"])


@router.post('/')
def insert_todos(todo:InsertTodo,db: dbManager = Depends(get_db)):
    SQLmanager = SQL(db)
    return SQLmanager.insert_table(todo)

@router.get("/", response_model=list[ShowTodo])
def get_todos(category_id: int,db: dbManager = Depends(get_db)):
    SQLmanager = SQL(db)
    return SQLmanager.show_table(category_id)

@router.patch("/{todo_id}")
def update_todos(todo_id:int,todo:UpdateTodo,db: dbManager = Depends(get_db)):
    SQLmanager = SQL(db)
    return SQLmanager.update_table(todo_id,todo)

@router.delete('/{target_id}')
def delete_todos(target_id: int,db: dbManager = Depends(get_db)):
    SQLmanager = SQL(db)
    return SQLmanager.delete_table(target_id)