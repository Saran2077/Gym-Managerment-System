class Manager:
    def __init__(self, id,  name, contact, location, username, password, g_id):
        self.id = id
        self.name = name
        self.contact = contact
        self.location = location
        self.username = username
        self.__password = password
        self.g_id = g_id

    def getPassword(self):
        pwd = self.__password
        return pwd