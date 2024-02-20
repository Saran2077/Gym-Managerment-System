from Controller.Manager import Manager

class ManagerView:
    def __init__(self):
        self.manager = Manager()

    def salaryOptions(self) -> None:
        print("1) Salary Increment")
        print("2) Salary decrement")

    def trainerOptions(self) -> None:
        while True:
            print("1) Add Trainer")
            print("2) Remove Trainer")
            print("3) Salary")
            print("4) Show all trainers")
            print("5) Search a trainer")
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
                    self.manager.addMember()
                elif choice == '2':
                    self.manager.removeMember()
                elif choice == '3':
                    pass
                elif choice == '4':
                    pass
                elif choice == '5':
                    pass

    def memberOptions(self) -> None:
        while True:
            print("1) Add Member")
            print("2) Remove Member")
            print("3) Search for a member with id or name")
            print("4) Pay Fee")
            print("5) Fee not paid")
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
                    self.manager.addMember()
                elif choice == '2':
                    self.manager.removeMember()
                elif choice == '3':
                    pass
                elif choice == '4':
                    pass
                elif choice == '5':
                    pass

    def options(self) -> None:
        while True:
            print("1) Member")
            print("2) Trainer")
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
                    self.memberOptions()
                elif choice == '2':
                    self.trainerOptions()
                elif choice == '3':
                    pass