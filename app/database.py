import sqlite3
class dbManager:
    def __init__(self):
     # データベースファイルに接続するコネクションの作成
      self.conn =sqlite3.connect('database.db')
     # カーソルの作成
      self.cur = self.conn.cursor()


