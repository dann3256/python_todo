# Fieldで詳細な設定をする(default:固有値で固定　default_factory:インスタンス作成時に毎回異なる値にする)
from sqlmodel import SQLModel,Field,Relationship
from typing import Optional
import uuid


# =============================================todo=====================================================

# 共通のフィールドを親クラス化して継承
class TodoBase(SQLModel):
    text:str
    status:str
    priority:str
    due_date:str
    category_id:uuid.UUID

# テーブル作成
class Todo(TodoBase,table=True):
    id :uuid.UUID=Field(default_factory=uuid.uuid4,primary_key=True)

class CreateTodo(TodoBase):
    pass

class ReadTodo(TodoBase):
    id :uuid.UUID

class UpdateTodo(SQLModel):
    text:Optional[str]=None
    status:Optional[str]=None
    priority:Optional[str]=None
    due_date:Optional[str]=None

class DeleteTodo(SQLModel):
    id :uuid.UUID

# =============================================category=====================================================

class Category(SQLModel,table=True):
    id:uuid.UUID=Field(default_factory=uuid.uuid4,primary_key=True)
    name:str

class InsertCategory(SQLModel):
    name: str

# categoryのid取得
class ReadCategory(SQLModel):
    id:uuid.UUID
    name: str

