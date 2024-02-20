from Model.Connection import Connection
from Model.gymDetails import GymDetails

class GymDetailsDAO:
    def __init__(self):
        self.conn = Connection.get_instance().conn
        self.cursor = self.conn.cursor()

    def getAll(self):
        query = f"SELECT * FROM GYM_DETAILS"
        self.cursor.execute(query)
        datas = self.cursor.fetchall()
        l = []
        for i in datas:
            l.append(GymDetails(*i))
        return l

    def check(self, g_id): #return True or False
        query = f"SELECT * FROM GYM_DETAILS WHERE G_ID = {g_id}"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        if data:
            return True
        return False

    def add(self, GymDetails): #return void
        query = f"INSERT INTO GYM_DETAILS VALUES ({GymDetails.id}, '{GymDetails.name}', '{GymDetails.location}');"
        self.cursor.execute(query)
        self.conn.commit()

    def remove(self, GymDetails): #return void
        if self.check(GymDetails.id):
            query = f"DELETE FROM GYM_DETAILS WHERE G_ID = {GymDetails.id}"
            self.cursor.execute(query)
            self.conn.commit()
        else:
            print("There is no gym with id")

    def change(self, GymDetails):
        pass

