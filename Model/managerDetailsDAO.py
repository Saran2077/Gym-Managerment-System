from Model.Connection import Connection
from Model.manager import Manager


class ManagerDetailsDAO:
    def __init__(self): #g_id
        self.conn = Connection.get_instance().conn
        self.cursor = self.conn.cursor()
        # self.g_id = g_id

    def getAll(self):
        query = f"SELECT * FROM OWNER_DETAILS"
        self.cursor.execute(query)
        datas = self.cursor.fetchall()
        l = []
        for i in datas:
            l.append(Manager(*i))
        return l

    def check(self, manager): #return Object or False
        query = f"SELECT * FROM OWNER_DETAILS WHERE USERNAME = '{manager.username}'"
        self.cursor.execute(query)
        datas = self.cursor.fetchall()
        if datas:
            data = datas[0]
            return Manager(*data)
        return False

    def add(self, Manager): #return void
        query = f"INSERT INTO OWNER_DETAILS VALUES({Manager.id}, '{Manager.name}', '{Manager.contact}', '{Manager.location}', '{Manager.username}', '{Manager.getPassword()}', {Manager.g_id});"
        self.cursor.execute(query)
        self.conn.commit()

    def remove(self, Manager): #return void
        query = f"DELETE FROM OWNER_DETAILS WHERE O_ID = {Manager.id}"
        self.cursor.execute(query)
        self.conn.commit()

    def changeOwner(self, oldManager, newManager): #return void
        query = f"DELETE FROM OWNER_DETAILS WHERE O_ID = {oldManager.id};"
        self.cursor.execute(query)
        self.conn.commit()
        self.add(newManager)

    def changeDetails(self):
        pass


# old = Manager()
# m = ManagerDetailsDAO()
# m.changeDetails()