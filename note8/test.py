import mysql.connector
dbconfig = {"host": "127.0.0.1", "user": "root",
            "password": "", "database": "myweb"}
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """SHOW TABLES"""
cursor.execute(_SQL)
results = cursor.fetchall()
print(results)
cursor.close()
conn.close()
# [('log',)]