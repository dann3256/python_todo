from main import db_admin
class SQL:
    def create_table(self):
        db_admin.cur.execute('create table if not exists todo(id INTEGER PRIMARY KEY,text TEXT,status INTEGER ,priority INTEGER ,due_date TEXT)')
        db_admin.conn.commit()
    def insert_table(self,text, status, priority, due_date):
         db_admin.cur.execute("insert into todo( text, status ,priority, due_date) values ( ?, ?, ?, ?)", (text, status, priority, due_date))
         db_admin.conn.commit()
    def show_table(self):
         db_admin.cur.execute("select * from todo")
         todoes= db_admin.cur.fetchall()
         for todo in todoes:
          print(todo)
    def update_table(self,text, target_id):
        db_admin.cur.execute("update todo set text = ? where id = ?", (text, target_id))
        db_admin.conn.commit()
    def delete_table(self,target_id):
        db_admin.cur.execute("delete from todo where id = ?", (target_id,))
        db_admin.conn.commit()