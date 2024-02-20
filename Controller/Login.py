from Model.managerDetailsDAO import ManagerDetailsDAO

class Login:
    def validateLogin(username, password):
        managerDetails = ManagerDetailsDAO()
        data = managerDetails.getAll()
        for i in data:
            if i.username == username and i.getPassword() == password:
                return True, i
        return False

