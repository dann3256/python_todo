from sqlmodel import Session, select
from db.models import Todo, CreateTodo, ReadTodo, UpdateTodo
import uuid

class SQL_todo:

    def __init__(self, session: Session):
        self.session = session
        
    # todoを追加する
    def insert_todo(self, todo: CreateTodo) :
        # テーブルの型にバリデーション
        db_todo = Todo.model_validate(todo)
        # 更新するためにキューに追加
        self.session.add(db_todo)
        # 変更
        self.session.commit()
        # DBの状態をpyhonのインスタンスにも同期させる
        self.session.refresh(db_todo)
        return None

    # カテゴリIDでtodoを取得する
    def show_todos(self, category_id: int) -> list[ReadTodo]:
        # SQL文を作成
        statement = select(Todo).where(Todo.category_id == category_id)
        # 実行
        rows = self.session.exec(statement).all()
        return rows

    # todoを更新する
    def update_todo(self, todo_id: uuid.UUID, uptodo: UpdateTodo):
        
        # idが一致するものテーブルを持ってくる
        db_todo = self.session.get(Todo, todo_id)
        if db_todo is None:
            return None
    
        # patchを実現させるために空の状態は除去
        update_data = uptodo.model_dump(exclude_unset=True)

        for key, value in update_data.items():
        # keyを自動的に探してそこにvalueを入れる
            setattr(db_todo, key, value)
        self.session.add(db_todo)
        self.session.commit()
        self.session.refresh(db_todo)
        return db_todo

    # todoを削除する
    def delete_todo(self, todo_id: uuid.UUID):
        db_todo = self.session.get(Todo, todo_id)
        if db_todo is None:
            return None
        self.session.delete(db_todo)
        self.session.commit()
    #  refreshはしない（同期できないため）