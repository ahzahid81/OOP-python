class Calculator:
    brand = 'Casio MS990'

    def add(self, num1, num2):
        return num1+num2
    
    def deduct(self, num1, num2):
        return num1-num2
    
    def multiply(self, num1, num2):
        return num1*num2
    
    def divide(self, num1, num2):
        return num1/num2
    

calculator = Calculator()

result1 = calculator.add(10,5)
result2 = calculator.deduct(10,5)
result3 = calculator.multiply(10,5)
result4 = calculator.divide(10,5)

print(result1)
print(result2)
print(result3)
print(result4)