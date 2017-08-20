import pymysql

# 打开数据库连接
db = pymysql.connect('127.0.0.1', 'root', '123546', 'czlyj')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS MSG")

# 使用预处理语句创建表
create_sql = """CREATE TABLE MSG (
         company_name  CHAR(120) NOT NULL,
         legal_name  CHAR(20),
         register_money CHAR(24),  
         create_time CHAR(20),  
         phone CHAR(25),  
         email CHAR(48),  
         address CHAR(100))"""

insert_sql = """INSERT INTO MSG(company_name,legal_name, register_money, create_time, phone,email,address)
            VALUES 
            (%s, %s, %s, %s, %s , %s , %s)"""

cursor.execute(create_sql)

# 关闭数据库连接
db.close()


def batch_insert(T):
    cursor.executemany(insert_sql, T)


