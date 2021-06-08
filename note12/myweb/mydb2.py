import mysql.connector
class MyDB2():
    def __init__(self):
        self.dbconfig = {"host": "127.0.0.1", "user": "root",
                         "password": "", "database": "myweb"}

    def __connect(self):
        self.dbConnect = mysql.connector.connect(**self.dbconfig)
        self.cursor = self.dbConnect.cursor()

    def __close(self):
        self.dbConnect.commit()
        self.cursor.close()
        self.dbConnect.close()

    def __enter__(self) -> 'cursor':
        self.__connect()
        return self.cursor

    def __exit__(self, expType, expVal, expTrace):
        self.__close()
