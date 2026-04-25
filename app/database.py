import sqlite3
class dbManager:
    def __init__(self):
     # データベースファイルに接続するコネクションの作成
      self.conn =sqlite3.connect('database.db')
      # SQL文でタプルじゃなく辞書を返すようにする
      self.conn.row_factory = sqlite3.Row
     # カーソルの作成
      self.cur = self.conn.cursor()
     # テーブルの作成
      self.create_table()

    def create_table(self):
     self.cur.execute('create table if not exists todo(id INTEGER PRIMARY KEY,text TEXT,status TEXT,priority TEXT ,due_date TEXT ,category_id INTEGER)')
     self.cur.execute('create table if not exists category(id INTEGER PRIMARY KEY,name TEXT)')
     
    def close(self):
      self.conn.close()

# API関数が終了した際にdbを閉じるためのジェネレータ関数
def get_db():
    db = dbManager()
    try:
        yield db
    finally:
        db.close()