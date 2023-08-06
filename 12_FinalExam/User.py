class User:
    def __init__(self, userName, minimumBalance=0):
        self.userName = userName
        self.minimumBalance = minimumBalance
        self.balance = minimumBalance
        self.transactionHistory = []
        self.loanTaken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactionHistory.append(f'Deposited: (cash In) {amount} BDT')

    def withdraw(self, amount):
        if self.balance - amount >= self.minimumBalance:
            self.balance -= amount
            self.transactionHistory.append(f'Withdrawn: (cash out) {amount} BDT')
        else:
            print(f'Insufficient balance to withdraw {amount} BDT. Bank is bankrupt.')

    def transfer(self, receiver, amount):
        if self.balance - amount >= self.minimumBalance:
            self.balance -= amount
            receiver.balance += amount
            self.transactionHistory.append(f'Transferred: Cash Out {amount} BDT to {receiver.userName}')
            receiver.transactionHistory.append(f'Received: Cash In {amount} BDT from {self.userName}')
        else:
            print("Insufficient balance. Bank is bankrupt.")

    def takeLoan(self, loanAmount):
        totalAmount = self.balance + self.loanTaken

        if loanAmount <= totalAmount * 2:
            self.loanTaken += loanAmount
            self.balance += loanAmount
            self.transactionHistory.append(f'Loan taken: Cash In {loanAmount} BDT')
        else:
            print(f'{loanAmount} BDT exceeds twice your total amount')

    def checkBalance(self):
        return self.balance

    def checkTransactionHistory(self):
        return self.transactionHistory
