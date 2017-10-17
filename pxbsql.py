import pymysql

db = pymysql.connect('127.0.0.1', 'root', '123546', 'database', charset='utf8', use_unicode=True)

cursor = db.cursor()
create_sql = """CREATE TABLE pxb (
         name  CHAR(255),
         person  CHAR(255),
         phone CHAR(255)"""

insert_sql = """INSERT INTO pxb(name,person, phone) VALUES (%s, %s, %s)"""


def insert(d):
    cursor.executemany(insert_sql, d)
    db.commit()
