from Controller.Admin import Admin

admin = Admin()

class AdminView:
    def __init__(self):
        pass

    def gymOptions(self):
        while True:
            print("1) Add Gym")
            print("2) Remove Gym")
            print("3) Revenue")
            choice = input().strip()
            if choice.lower() == 'q':
                return
            elif choice == "":
                print("Choice can't be empty...")
            elif not choice.isdigit():
                print("Choice can only be number...")
            elif int(choice) <= 0 or int(choice) > 3:
                print("Choose a valid option...")
            else:
                if choice == '1':
                    admin.addGym()
                elif choice == '2':
                    admin.removeGym()
                elif choice == '3':
                    pass

    def managerOptions(self):
        while True:
            print("1) Show Managers")
            print("2) Change Manager")
            print("3) Salary")
            #print("4) ")
            choice = input().strip()
            if choice.lower() == 'q':
                return
            elif choice == "":
                print("Choice can't be empty...")
            elif not choice.isdigit():
                print("Choice can only be number...")
            elif int(choice) <= 0 or int(choice) > 4:
                print("Choose a valid option...")
            else:
                if choice == '1':
                    pass
                elif choice == '2':
                    pass
                elif choice == '3':
                    pass



    def options(self):
        while True:
            print("1) Gym")
            print("2) Manager")
            print("3) Income")
            choice = input().strip()
            if choice.lower() == 'q':
                return
            elif choice == "":
                print("Choice can't be empty...")
            elif not choice.isdigit():
                print("Choice can only be number...")
            elif int(choice) <= 0 or int(choice) > 3:
                print("Choose a valid option...")
            else:
                if choice == '1':
                    self.gymOptions()
                elif choice == '2':
                    self.managerOptions()
                elif choice == '3':
                    pass
a = AdminView()
a.options()