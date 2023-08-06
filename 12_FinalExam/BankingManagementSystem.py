from Admin import Admin
from User import User

class BankingManagementSystem:
    def __init__(self):
        self.admin = Admin()
        self.users = {}

    def createAccount(self, userName, requiredMinimumBalance=0, initialBalance=0):
        if userName in self.users:
            print("Account already exists.")
            return

        newUser = User(userName, requiredMinimumBalance)
        newUser.deposit(initialBalance - requiredMinimumBalance)
        self.users[userName] = newUser
        self.admin.createAccount(newUser, initialBalance)

    def userAction(self, userName):
        if userName not in self.users:
            print('Account does not exist.')
            return None

        return self.users[userName]

    def adminAction(self):
        return self.admin
