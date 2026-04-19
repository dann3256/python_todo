from models import SQL
from database import dbManager
# インスタンス化
db_admin = dbManager() 
SQLmanager=SQL()
try:
   while True:
      print("1.テーブル作成\n 2.データ挿入\n 3.データ取得\n 4.データ更新\n 5.テーブル削除")
      s= input('番号を入力してください: ')
      if    s =="0":
       break
      # SQL文の実行
      elif  s == "1":
         SQLmanager.create_table()
      elif s == "2":
         text = input("テキストを入力してください: ")
         status = input("ステータスを入力してください(stay or done): ")
         priority =input('優先度を入力してください: ')
         due_date = input('期日を入力してください (YYYY-MM-DD): ')
         SQLmanager.insert_table(text, status, priority, due_date) 
      elif s == "3":
         SQLmanager.show_table()
      elif s == "4":
          target_id = input("更新するIDを入力してください: ")
          text = input("新しいテキストを入力してください: ")
          SQLmanager.update_table(text, target_id)   
      elif s == "5":
         target_id = input("削除するIDを入力してください: ")
         SQLmanager.delete_table(target_id)
       
finally:
# データベースの接続を切る
 db_admin.conn.close()