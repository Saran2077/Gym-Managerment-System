from Model.Connection import Connection
from Model.member import Member

class MemberDAO:
    def __init__(self, g_id):
        self.conn = Connection.get_instance().conn
        self.cursor = self.conn.cursor()
        self.g_id = g_id
        self.columns = 'M_ID, G_ID, M_NAME, M_AGE, M_CONTACT, M_ADDRESS, M_JOINDATE'

    def check(self, member):
        query = f"SELECT * FROM MEMBER WHERE M_ID = '{member.id}'"
        self.cursor.execute(query)
        datas = self.cursor.fetchall()
        if datas:
            data = datas[0]
            return Member(*data)
        return False

    def add(self, member):
        query = f"INSERT INTO MEMBER VALUES({member.id}, {member.g_id}, '{member.name}', '{member.age}', '{member.contact}', '{member.location}', CURRENT_DATE());"
        self.cursor.execute(query)
        self.conn.commit()

    def remove(self, member):
        query = f"DELETE FROM MEMBER WHERE M_ID = {member.id}"
        self.cursor.execute(query)
        self.conn.commit()

    def getAll(self):
        query = f"SELECT * FROM MEMBER"
        self.cursor.execute(query)
        datas = self.cursor.fetchall()
        l = []
        for i in datas:
            l.append(Member(*i))
        return l