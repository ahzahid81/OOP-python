class Admin:
    def __init__(self):
        self.bankTotalBalance = 0
        self.loan_feature_enabled = True

    def createAccount(self, user, initial_balance=0):
        user.deposit(initial_balance)
        self.bankTotalBalance += initial_balance
        print(f'Account created successfully for {user.userName}.')

    def check_total_balance(self):
        return self.bankTotalBalance

    def check_total_loan_amount(self, users):
        total_loan_amount = sum(user.loanTaken for user in users.values())
        return total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True
        print("Loan feature enabled.")

    def disable_loan_feature(self):
        self.loan_feature_enabled = False
        print("Loan feature disabled.")
