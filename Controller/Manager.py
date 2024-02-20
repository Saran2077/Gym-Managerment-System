from Model.memberDAO import *
memberDAO = MemberDAO()

class Manager:
    def __init__(self, g_id=None):
        self.g_id = g_id
        self.memberDAO = MemberDAO()
    def addMember(self):
        id = 1
        data = self.memberDAO.getAll()
        if data:
            id = data[-1].id + id
        while True:
            name = input('Enter the name of the Member: ').strip()
            if name.lower() == 'q':
                return
            if name == "":
                print("Name can't be empty")
                continue
            if not name.isalpha():
                print("Name should be in string")
                continue
            break
        while True:
            age = input('Enter the age of the member: ').strip()
            if age.lower() == 'q':
                return
            if age == "":
                print("Age can't ve empty")
                continue
            if not age.isdigit():
                print("Age should br in number")
                continue
            if int(age) < 1:
                print("Age can't be negative")
                continue
            if int(age) > 90:
                print("Invalid age")
                continue
            break
        while True:
            address = input("Enter the city of the member: ").strip()
            if address.lower() == 'q':
                return
            if address == "":
                print("Address can't be empty")
                continue
            if address.isalpha():
                print("Address should be in string")
                continue
            break
        while True:
            contact = input("Enter the number of the member: ").strip()
            if contact.lower() == 'q':
                return
            if contact == "":
                print("Number can't be empty")
                continue
            if not contact.isdigit():
                print("Phone number should be in number")
                continue
            if len(contact) != 10:
                print("Phone number should be in 10 digits")
                continue
            if contact[0] == '0':
                print("Phone number can't starts with 0")
                continue
            break
        member = Member(id, self.g_id, name, age, contact, address, "CURRENT_DATE()")
        memberDAO.add(member)

    def removeMember(self, member):
        while True:
            if memberDAO.check(member):
                memberDAO.remove(member)
                return True
            return False

    def not_paid(self):
        pass

    def getAllMemebers(self):
        return memberDAO.getAll()

    def search(self, id):
        data, l = memberDAO.getAll(), []
        if id.isdigit():
            for i in data:
                if i.id == id:
                    return i
        else:
            for i in data:
                if i.name == id:
                    l.append(i)
            return l
        return False

    def addTrainer(self):
        pass

    def removeTrainer(self):
        pass

    def viewTrainer(self):
        pass

    def viewAllTrainer(self):
        pass


