import mysql.connector


class MyDB():
    def __init__(self):
        self.dbconfig = {"host": "127.0.0.1", "user": "root",
                         "password": "", "database": "myweb"}

    def connect(self):
        self.dbConnect = mysql.connector.connect(**self.dbconfig)
        self.cursor = self.dbConnect.cursor()

    def close(self):
        self.cursor.close()
        self.dbConnect.close()

    def executeSQL(self, _SQL: str, params: tuple) -> list:
        """执行SQL"""
        self.connect()
        self.cursor.execute(_SQL, params)
        results = self.cursor.fetchall()
        self.dbConnect.commit()
        self.close()
        return results
