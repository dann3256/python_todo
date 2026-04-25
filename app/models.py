from schemas import InsertTodo,ShowTodo,UpdateTodo,DeleteTodo,InsertCategory,ShowCategory
from database import dbManager
class SQL:
    # 外部キーを有効にするコンストラクタ
    def __init__(self,db_admin:dbManager):
        self.db_admin=db_admin
        self.db_admin.cur.execute("PRAGMA foreign_keys = ON;")

    # todoテーブルを作成し、category_idとその他の入力情報をインサート
    def insert_table(self,todo:InsertTodo):
         self.db_admin.cur.execute("insert into todo(text, status, priority, due_date, category_id) values (?, ?, ?, ?, ?)",
        (todo.text, todo.status, todo.priority, todo.due_date, todo.category_id))
         self.db_admin.conn.commit()

    # category_idを用いて特定のカテゴリのtodoを全て表示
    def show_table(self,category_id:int) -> list[ShowTodo]:
         self.db_admin.cur.execute("""select * from todo 
                                   JOIN category ON todo.category_id=category.id 
                                   where category.id=? """,(category_id,)
                                   )
         rows= self.db_admin.cur.fetchall()
        #  **dictを使ってデータベースの値をアンパックして型へ自動マッピングする
         return [ShowTodo(**dict(row)) for row in rows]
          

    # テーブルの更新
    def update_table(self,todo_id:int,uptodo:UpdateTodo):
        self.db_admin.cur.execute(
            """UPDATE todo 
              SET text = COALESCE(?, text),
                  status = COALESCE(?, status),
                  priority = COALESCE(?, priority),
                  due_date = COALESCE(?, due_date)
              WHERE id = ?""",(uptodo.text,uptodo.status,uptodo.priority,uptodo.due_date,todo_id)) 
        self.db_admin.conn.commit()

    # テーブルの削除
    def delete_table(self,target_id):
        self.db_admin.cur.execute("delete from todo where id = ?", (target_id,))
        self.db_admin.conn.commit()

    # カテゴリの作成
    def create_category(self,category:InsertCategory):
         self.db_admin.cur.execute('insert into category(name) values (?)',(category.name,))  
         self.db_admin.conn.commit()
         return {"message": "作成に成功しました"} 

    # カテゴリの表示（category_idの表示が目的）
    def show_category(self)->list[ShowCategory]:
        self.db_admin.cur.execute('select * from category')
        categories=self.db_admin.cur.fetchall()
        
        return [ShowCategory(**dict(category)) for category in categories]



     