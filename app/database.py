import sqlite3
class dbManager:
    def __init__(self):
     # データベースファイルに接続するコネクションの作成
      self.conn =sqlite3.connect('database.db')
     # カーソルの作成
      self.cur = self.conn.cursor()
     # テーブルの作成
      self.create_table()
    def create_table(self):
     self.cur.execute('create table if not exists todo(id INTEGER PRIMARY KEY,text TEXT,status INTEGER ,priority INTEGER ,due_date ,category_id INTEGER)')
     self.cur.execute('create table if not exists category(id INTEGER PRIMARY KEY,name TEXT)')
     
    def close(self):
      self.conn.close()


