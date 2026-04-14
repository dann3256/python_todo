import sqlite3
import sys
sys.stdout.reconfigure(encoding='utf-8')
# データベースファイルに接続するコネクションの作成
conn =sqlite3.connect('database.db')
# カーソルの作成
cur = conn.cursor()

print("1.テーブル作成\n 2.データ挿入\n 3.データ取得\n 4.データ削除\n 5.テーブル更新")
s= input('番号を入力してください: ')

# SQL文の実行
if   s == "1":
    cur.execute("create table if not exists todo(id INTEGER PRIMARY KEY, text TEXT)")
    cur.commit() # データベースに変更を保存

elif s == "2":
    text = input("テキストを入力してください: ")
    cur.execute("insert into todo(id, text) values (?, ?)", (None, text))
    conn.commit()

elif s == "3":
    cur.execute("select * from todo")
    todos = cur.fetchall()
    for todo in todos:
        print(todo)

elif s == "4":
    id = input("削除するIDを入力してください: ")
    cur.execute("delete from todo where id = ?", (id,))
    conn.commit()

elif s == "5":
    id = input("更新するIDを入力してください: ")
    text = input("新しいテキストを入力してください: ")
    cur.execute("update todo set text = ? where id = ?", (text, id))
    conn.commit()

# データベースの接続を切る
conn.close()