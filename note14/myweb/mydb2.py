import mysql.connector
from user_exception import UserException


class MyDB2():
    def __init__(self):
        self.dbconfig = {"host": "127.0.0.1", "user": "root",
                         "password": "", "database": "myweb"}

    def __connect(self):
        try:
            self.dbConnect = mysql.connector.connect(**self.dbconfig)
            self.cursor = self.dbConnect.cursor()
        except mysql.connector.errors.InterfaceError:
            raise UserException(UserException.ERROR_DB_CONNECT, '数据库失连')
        except Exception:
            raise UserException(UserException.ERROR_DB_OTHER, '数据库未知错误')

    def __close(self):
        self.dbConnect.commit()
        self.cursor.close()
        self.dbConnect.close()

    def __enter__(self) -> 'cursor':
        self.__connect()
        return self.cursor

    def __exit__(self, expType, expVal, expTrace):
        self.__close()
        if expType != None:
            raise UserException(UserException.ERROR_SQL_EXECUTE, 'sql执行出错')
