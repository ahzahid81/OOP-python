from math import factorial

class QuestionNoThree:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c
    
    def factorial(self):
        return factorial(self.b)
    

test = QuestionNoThree(2, 3, 4)

print('Sum: ', test.sum())
print('Factorial: ', test.factorial())