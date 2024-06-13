from decouple import config
import pymysql
import pymysql.cursors

class DataBase():
    def __init__(self) -> None:
        self.conecction = pymysql.connect(
            host = config('MYSQL_HOST'),
            user = config('MYSQL_USER'),
            passwd = config('MYSQL_PASSWORD'),
            database = config('MYSQL_DB'),
            cursorclass = pymysql.cursors.DictCursor
        )
        self.cursor = self.conecction.cursor()

    def execute(self, query, args=None):

        self.cursor.execute(query, args)
        self.conecction.commit()

        return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
    def close(self):
        self.conecction.close()