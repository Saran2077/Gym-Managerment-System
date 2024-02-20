from Model.Connection import Connection
from Model.gymFeeStructure import gymFeeStructure

class GymFeeStructureDAO:
    def __init__(self):
        self.conn = Connection.get_instance().conn
        self.cursor = self.conn.cursor()

    def add(self, GymFeeStructures):
        for GymFeeStructure in GymFeeStructures:
            query = f"INSERT INTO GYM_FEE_STRUCTURE VALUES({GymFeeStructure.id}, '{GymFeeStructure.duration}', {GymFeeStructure.fee});"
            self.cursor.execute(query)
            self.conn.commit()

    def remove(self, GymFeeStructure):
        query = f"DELETE FROM GYM_FEE_STRUCTURE WHERE G_ID = {GymFeeStructure.id} AND DURATION = {GymFeeStructure.duration};"
        self.cursor.execute(query)
        self.conn.commit()

    def changePlan(self, GymFeeStructure):
        query = f"UPDATE GYM_FEE_STRUCTURE SET FEE = {GymFeeStructure.fee} WHERE G_ID = {GymFeeStructure.id} AND DURATION = '{GymFeeStructure.duration}';"
        self.cursor.execute(query)
        self.conn.commit()

