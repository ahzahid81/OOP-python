class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self.__balance = initial_deposit

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if self.__balance < amount:
            pass
rafsun = Bank('Chooto bro', 1000)

print(rafsun.holder_name)
print(rafsun.get_balance())
#print(dir(rafsun))
print(rafsun._Bank__balance)