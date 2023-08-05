class Restaurant:
    def __init__(self, name, rent, menu = []) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = menu
        self.rent = rent
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee

    def add_order(self, order):
        self.orders.append(order)


    def receive_payment(self, order, amount, customer):
        if order.bill < amount:
            self.revenue += amount
            customer.due_amount = 0
            return amount-order.bill

    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expens {amount} for {description}')
        else:
            print(f'Not enough money')

    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.receieve_salary()

    def show_employees(self):
        print(f'-----------SHOWING EMPLOYEES--------')
        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary: {self.chef.salary}')
        if self.server is not None:
            print(f'Server: {self.server.name} with salary: {self.server.salary}')

    