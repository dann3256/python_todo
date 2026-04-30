from fastapi import APIRouter,Depends
from db.models import Todo, CreateTodo, ReadTodo, UpdateTodo
from db.Gateways.todo_gw import SQL_todo
from database import get_session
from sqlmodel import Session
import uuid
# URLの先頭の名前を統一／APIをグループ化するためにタグ付け
router = APIRouter(prefix="/todos", tags=["todos"])


@router.post('/')
def insert_todos(todo:CreateTodo,db: Session = Depends(get_session)):
    SQLmanager = SQL_todo(db)
    return SQLmanager.insert_todo(todo)

@router.get("/", response_model=list[ReadTodo])
def get_todos(category_id: uuid.UUID,db: Session = Depends(get_session)):
    SQLmanager = SQL_todo(db)
    return SQLmanager.show_todos(category_id)

@router.patch("/{todo_id}")
def update_todos(todo_id:uuid.UUID,todo:UpdateTodo,db: Session = Depends(get_session)):
    SQLmanager = SQL_todo(db)
    return SQLmanager.update_todo(todo_id,todo)

@router.delete('/{target_id}')
def delete_todos(target_id: uuid.UUID,db: Session = Depends(get_session)):
    SQLmanager = SQL_todo(db)
    return SQLmanager.delete_todo(target_id)