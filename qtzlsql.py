import pymysql

db = pymysql.connect('127.0.0.1', 'root', '123546', 'database')

cursor = db.cursor()
create_sql = """CREATE TABLE qtzl (
         title  CHAR(255),
         url CHAR(255))"""

# cursor.execute(create_sql)

insert_sql = """INSERT INTO qtzl(title , url) 
VALUES 
(%s , %s)"""


def insert(data):
    for i in range(len(data)):
        title = data[i]["title"]
        url = data[i]["url"]
        cursor.execute("INSERT INTO qtzl (title,url) VALUES ('" + title + "','" + url + "')")
    db.commit()
