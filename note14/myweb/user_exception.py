class UserException(Exception):
    ERROR_DB_CONNECT = 1
    ERROR_DB_OTHER = 2
    ERROR_SQL_EXECUTE = 3

    def __init__(self, code, message=''):
        super()
        self.__code = code
        self.__message = message

    def getErrorCode(self):
        return self.__code

    def getErrorMessage(self):
        return self.__message
