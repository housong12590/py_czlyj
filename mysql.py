import pymysql

db = pymysql.connect('127.0.0.1', 'root', '123546', 'database')

cursor = db.cursor()
create_sql = """CREATE TABLE MSG (
         company_name  CHAR(120) NOT NULL,
         legal_name  CHAR(20),
         register_money CHAR(24),  
         create_time CHAR(20),  
         phone CHAR(25),  
         email CHAR(48),  
         address CHAR(100))"""

# cursor.execute(create_sql)

insert_sql = """INSERT INTO msg(company_name,legal_name, register_money, create_time, phone,email,address,status) 
VALUES 
(%s, %s, %s, %s, %s , %s ,%s,%s)"""


def insert(d):
    cursor.executemany(insert_sql, d)
    db.commit()
