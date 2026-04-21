from models import SQL
from database import dbManager
# インスタンス化
db_admin=dbManager()
SQLmanager=SQL(db_admin)

try:
   while True:
      print("1.データ挿入\n 2.データ取得\n 3.データ更新\n 4.テーブル削除\n 5.カテゴリ追加\n 6.カテゴリ一覧")
      s= input('番号を入力してください: ')
      if    s =="0":
       break
      # SQL文の実行
      elif s == "1":
         category_id =input('カテゴリーidを入力してください')
         text = input("テキストを入力してください: ")
         status = input("ステータスを入力してください(stay or done): ")
         priority =input('優先度を入力してください: ')
         due_date = input('期日を入力してください (YYYY-MM-DD): ')
         SQLmanager.insert_table(category_id,text, status, priority, due_date) 
         
      elif s == "2":
         category=input('カテゴリーを入力してください：')
         SQLmanager.show_table(category)

      elif s == "3":
          target_id = input("更新するIDを入力してください: ")
          text = input("新しいテキストを入力してください: ")
          SQLmanager.update_table(text, target_id)   

      elif s == "4":
         target_id = input("削除するIDを入力してください: ")
         SQLmanager.delete_table(target_id)

      elif s == "5":
         name =input("カテゴリを追加してください：")
         SQLmanager.create_category(name)

      elif s == "6":
         SQLmanager.show_category()
       
finally:
# データベースの接続を切る
 SQLmanager.db_admin.close()