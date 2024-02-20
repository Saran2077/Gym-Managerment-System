import mysql.connector

class Connection:
    __instance = None

    @staticmethod
    def get_instance():
        if Connection.__instance is None:
            Connection.__instance = Connection()
        return Connection.__instance

    def __init__(self):
        if Connection.__instance is None:
            self.conn = mysql.connector.connect(
                host="127.0.0.10",
                user="root",
                passwd="2580",
                database="admin"
            )
            Connection.__instance = self
            print("Connected to the server")
        else:
            raise Exception("Object cannot be initialized more than once")
