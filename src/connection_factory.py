import mysql.connector
import json

class MyConnector:
    def __init__(self):
        self.f_json = self.importConfig()
        self.host = self.f_json['host']
        self.password = self.f_json['password']
        self.port = self.f_json['port']
        self.user = self.f_json['user']
        self.database = self.f_json['database']

    def open(self):
        return mysql.connector.connect(host=self.host, password=self.password,port=self.port,user=self.user,database=self.database)

    def close(self, connection):
        connection.close()

    def importConfig(self):
        f = open("./config.json","r")
        f_json = json.loads(f.read())
        f.close()
        return f_json