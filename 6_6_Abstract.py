from abc import ABC, abstractmethod
#abstract base class

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('hey nana!, eating banana')

    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category= 'Monkey'
        self.name = name
        super().__init__()
    
    def eat(self):
        print('Hey na na na, I am eating banana')

layka = Monkey('lucky')
layka.eat()