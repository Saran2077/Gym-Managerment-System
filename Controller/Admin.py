from Model.managerDetailsDAO import *
from Model.gymDetailsDAO import *
from Model.gymFeeStructureDAO import *

class Admin:
    def __init__(self):
        self.managerDAO = ManagerDetailsDAO()
        self.gymDetailsDAO = GymDetailsDAO()
        self.gymFeeStructure = GymFeeStructureDAO()

    def addGym(self):
        gyms = self.gymDetailsDAO.getAll()
        id = 1
        if gyms:
            id = gyms[-1].id + 1
        print('Enter q to go back...')
        while True:
            name = input('Enter the gym Name: ').strip()
            if name.lower() == 'q':
                return
            if name == '':
                print("Name can't be empty")
                continue
            if name.isdigit():
                print("Name can't be number")
                continue
            break
        while True:
            location = input('Enter the gym location: ').strip()
            if location.lower() == 'q':
                return
            if location == '':
                print("Location can't be empty")
                continue
            if not location.isalpha():
                print("Location should be string")
                continue
            break
        print('Enter the fee structure for your gym')
        Gym = GymDetails(id, name, location)
        self.addGymFeeStructure(Gym)

    def removeGym(self):
        gyms = self.gymDetailsDAO.getAll()
        while True:
            a = input("Enter the gym id to remove: ").strip()
            if a.lower() == 'q':
                return
            if a == "":
                print("Gym id can't be empty...")
                continue
            if not a.isdigit():
                print("Gym id should be number...")
                continue
            gym = list(filter(lambda x: x.id == int(a), gyms))
            print(gym)
            if not gym:
                print("Enter a valid id...")
            break
        self.gymDetailsDAO.remove(gym[0])

    def addManager(self, Gym, l):
        managers = self.managerDAO.getAll()
        id = 1
        if managers:
            id = managers[-1].id + 1
        while True:
            o_name = input("Enter the manager's name: ").strip()
            if o_name.lower() == 'q':
                return
            if o_name == '':
                print("Manager name can't be empty...")
                continue
            if not o_name.isalpha():
                print("Manager's name should be string...")
                continue
            break

        while True:
            o_contact = input("Enter the manager's contact: ").strip()
            if o_contact.lower() == 'q':
                return
            if o_contact == '':
                print("Manager name can't be empty...")
                continue
            if not o_contact.isdigit():
                print('Phone no should be in numbers...')
                continue
            if len(o_contact) != 10:
                print("Phone number should be in 10 digits")
                continue
            if o_contact[0] == '0':
                print("Phone Number can't starts with 0...")
                continue
            break
        while True:
            o_address = input("Enter the manager's address: ").strip()
            if o_address.lower() == 'q':
                return
            if o_address == '':
                print("Address can't be empty...")
                continue
            if not o_address.isalpha():
                print("Address should be string...")
                continue
            break
        username = o_name + o_contact[:5]
        password = o_contact
        manager = Manager(id, o_name, o_contact, o_address, username, password, Gym.id)
        self.gymDetailsDAO.add(Gym)
        self.managerDAO.add(manager)
        self.gymFeeStructure.add(l)

    def changeManager(self, oldManager, newManager):
        self.changeManager(oldManager, newManager)

    def addGymFeeStructure(self, Gym):
        details = {}
        while True:
            month = input('Enter the no of months: ').strip()
            if month.lower() == 'q':
                return
            if month == '':
                print('Months cant be empty...')
                continue
            if not month.isdigit():
                print('Months should be in integer')
                continue
            if month in details:
                print('Month is already exists...')
                continue
            if int(month) < 1 or int(month) > 12:
                print('Enter a valid month')
                continue
            while True:
                fee = input(f'Enter the fee for {month} months: ').strip()
                if fee.lower() == 'q':
                    return
                if fee == '':
                    print('Fees cant be empty...')
                    continue
                if not fee.isdigit():
                    print('Fees should be in integer')
                    continue
                details[month + (" month" if month == '1' else " months")] = fee
                break
            ask = input('Enter y to add fee structure or n to break: ')
            if ask != 'y':
                break
        l = []
        for i in details:
            l.append(gymFeeStructure(Gym.id, i, details[i]))
        self.addManager(Gym, l)

a = Admin()
