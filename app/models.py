
from database import dbManager
db_admin = dbManager() 
class SQL:
    # 外部キーを有効にするコンストラクタ
    def __init__(self,db_admin):
        self.db_admin=db_admin
        db_admin.cur.execute("PRAGMA foreign_keys = ON;")

    # todoテーブルを作成し、category_idとその他の入力情報をインサート
    def insert_table(self,category_id,text, status, priority, due_date):
         db_admin.cur.execute("insert into todo( text, status ,priority, due_date,category_id) values ( ?, ?, ?, ? ,?)", (text, status, priority, due_date,category_id))
         db_admin.conn.commit()

    # category_idを用いて特定のカテゴリのtodoを全て表示
    def show_table(self,category):
         db_admin.cur.execute("select todo.text from todo JOIN category ON todo.category_id=category.id where category.name=?", (category,))
         todoes= db_admin.cur.fetchall()
         for todo in todoes:
          print(todo)

    # テーブルの更新
    def update_table(self,text, target_id):
        db_admin.cur.execute("update todo set text = ? where id = ?", (text, target_id))
        db_admin.conn.commit()

    # テーブルの削除
    def delete_table(self,target_id):
        db_admin.cur.execute("delete from todo where id = ?", (target_id,))
        db_admin.conn.commit()

    # カテゴリの作成
    def create_category(self,name):
         db_admin.cur.execute('insert into category(name) values (?)',(name,))  
         db_admin.conn.commit() 

    # カテゴリの表示（category_idの表示が目的）
    def show_category(self):
        db_admin.cur.execute('select * from category')
        categories=db_admin.cur.fetchall()
        for category in categories:
            print(category)



     