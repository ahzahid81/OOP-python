from BankingManagementSystem import BankingManagementSystem

# Main part for test cases
bms = BankingManagementSystem()

# Admin checks total balance (should be 0)
print("Total available balance:", bms.adminAction().check_total_balance())

# Admin creates user accounts
bms.createAccount("Alice", 500, 1000)
bms.createAccount("Bob", 300, 800)

# Alice checks her balance
alice = bms.userAction("Alice")
print("Alice's balance:", alice.checkBalance())

# Bob deposits money
bob = bms.userAction("Bob")
bob.deposit(200)
print("Bob's balance after deposit:", bob.checkBalance())

# Alice transfers money to Bob
alice.transfer(bob, 100)
print("Alice's balance after transfer:", alice.checkBalance())
print("Bob's balance after transfer:", bob.checkBalance())

# Admin checks total balance after all transactions
print("Total available balance:", bms.adminAction().check_total_balance())

# Alice tries to take a loan, but it's disabled by admin
alice.takeLoan(200)

# Admin disables loan feature
bms.adminAction().disable_loan_feature()

# Bob tries to take a loan (should show a message that the loan feature is disabled)
bob.takeLoan(300)

# Admin enables loan feature
bms.adminAction().enable_loan_feature()

# Bob tries to take a loan again (should work now)
bob.takeLoan(300)

# Admin checks total loan amount
print("Total loan amount:", bms.adminAction().check_total_loan_amount(bms.users))

# Alice checks her transaction history
print("Alice's transaction history:", alice.checkTransactionHistory())