# Base class representing Family
class Family:
    def __init__(self, address) -> None:
        self.address = address

# Derived class Student inheriting from Family
class Student(Family):
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        super().__init__(address)

# Creating an instance of Student class
student = Student("Zahid", 20, "Sobujbug")

# Accessing attributes from both Student and Family classes
print("Name:", student.name)         # Output: Name: Zahid
print("Age:", student.age)           # Output: Age: 20
print("Address:", student.address)   # Output: Address: Sobujbug
