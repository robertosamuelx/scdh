from connection_factory import MyConnector
import datetime

class Entity:
    def __init__(self):
        self.id = 0
        self.createdAt = datetime.datetime.now()
        self.ph = 0.0
        self.status = ''
        self.connector = MyConnector()

    def count(self):
        sql = 'SELECT count(1) FROM history'
        connection = self.connector.open()
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()[0]
        print(result)
        self.connector.close(connection)
        return result

    def save(self):
        sql = 'INSERT INTO history (id, createdAt, ph, status) VALUES (%s, %s, %s, %s)'
        self.id = self.count() + 1
        values = (self.id, self.createdAt, self.ph, self.status)
        connection = self.connector.open()
        cursor = connection.cursor()
        cursor.execute(sql,values)
        connection.commit()
        self.connector.close(connection)