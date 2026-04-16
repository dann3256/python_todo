import sqlite3
# データベースファイルに接続するコネクションの作成
conn =sqlite3.connect('database.db')
# カーソルの作成
cur = conn.cursor()


try:
   while True:
      print("1.テーブル作成\n 2.データ挿入\n 3.データ取得\n 4.データ削除\n 5.テーブル更新")
      s= input('番号を入力してください: ')
      if    s =="0":
         break
      # SQL文の実行
      elif  s == "1":
         cur.execute("create table if not exists todo(id INTEGER PRIMARY KEY, text TEXT ,status INTEGER ,priority INTEGER ,due_date TEXT)")
         conn.commit()

      elif s == "2":
         text = input("テキストを入力してください: ")
         status = input("ステータスを入力してください(stay or done): ")
         priority =input('優先度を入力してください: ')
         due_date = input('期日を入力してください (YYYY-MM-DD): ')
         cur.execute("insert into todo( text, status ,priority, due_date) values ( ?, ?, ?, ?)", (text, status, priority, due_date))
         conn.commit()

      elif s == "3":
         cur.execute("select * from todo")
         todoes= cur.fetchall()
         for todo in todoes:
            print(todo)

      elif s == "4":
         target_id = input("削除するIDを入力してください: ")
         cur.execute("delete from todo where id = ?", (target_id,))
         conn.commit()

      elif s == "5":
         target_id = input("更新するIDを入力してください: ")
         text = input("新しいテキストを入力してください: ")
         cur.execute("update todo set text = ? where id = ?", (text, target_id))
         conn.commit()

finally:
# データベースの接続を切る
 conn.close()