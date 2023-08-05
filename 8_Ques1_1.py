class Myclass:
    class_variable = 0

    def __init__(self, value) -> None:
        self.value = value

    @classmethod #This is a decorator for class method
    def class_method_example(cls, x):
        print(f"This is a class method, Class Variable: {cls.class_variable}, Input: {x}")

    
    @staticmethod #This is a decorator for static method
    def static_method_exaple(y):
        print(f'This is a static method. Input: {y}')

    @classmethod
    def class_method_modify_class_variable(cls, new_value):
        cls.class_variable = new_value

    @staticmethod
    def static_method_cannot_modify_class_variable(new_value):
        # This will raise an AttributeError since static methods can't access the class variable directly.
        Myclass.class_variable = new_value


obs = Myclass(42)

#calling the class method with MyClass
Myclass.class_method_example(10)
#Output: This is a class method, Class Variable: 0, Input: 10
#Note: Class Method has access to the class variable

#calling the static method with Myclass
Myclass.static_method_exaple(10)
#output: This is a static method. Input: 10
# Note: Static method does not have access to class variable directly.
# It only works with the parameters passed to it

#The instance can also call the class method
obs.class_method_example(30)
#Output: This is a class method, Class Variable: 0, Input: 30

obs.static_method_exaple(10)


# Using class method to modify class variable
print(Myclass.class_variable)  # Output: 0
Myclass.class_method_modify_class_variable(42)
print(Myclass.class_variable)  # Output: 42

# Using static method to modify class variable - This will raise an AttributeError
Myclass.static_method_cannot_modify_class_variable(100)
# Output: AttributeError: type object 'MyClass' has no attribute 'class_variable'