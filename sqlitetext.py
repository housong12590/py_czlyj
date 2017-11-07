import sqlite3
#
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # cursor.execute('INSERT INTO user (id, name) VALUES ("3", "mmmm")')
# # cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
#
# # count = cursor.rowcount
# # print(count)
#
# cursor.execute('select * from user WHERE id=? AND name =?',("1","housong"))
# result = cursor.fetchall()
# for i in result:
#     print(i)
# cursor.close()
# conn.commit()
# conn.close()
import os
db_path = os.path.join(os.path.dirname(__file__),"test.db")
if os.path.isfile(db_path):
    os.remove(db_path)