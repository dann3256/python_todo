from pydantic import BaseModel
# 型アノテーション用のライブラリ
from typing import Optional

# =======================todo=======================
# todoリストのテーブル作成
class InsertTodo(BaseModel):
    text: str
    status: str
    priority: str
    due_date: str
    category_id: int


# todoリストを表示する
class ShowTodo(BaseModel):
    id :int 
    text:str
    status:str
    priority:str
    due_date:str
    category_id:int

# todoリストの更新
class UpdateTodo(BaseModel):
    # strかNoneを受け入れる
    text: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[str] = None

# todoリストの削除
class DeleteTodo(BaseModel):
    id: int

# =======================category=======================

# categoryのテーブル作成
class InsertCategory(BaseModel):
    name: str

# categoryのid取得
class ShowCategory(BaseModel):
    id: int
    name: str