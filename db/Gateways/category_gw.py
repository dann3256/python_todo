from app.schemas import InsertCategory,ShowCategory
from app.database import dbManager

class SQL_category:
    def __init__(self,db_admin:dbManager):
        self.db_admin=db_admin
        self.db_admin.cur.execute("PRAGMA foreign_keys = ON;")
    
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

