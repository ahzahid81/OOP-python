# base class, parent class, common attribute + funcationality class
# derived class, child class, Uncommon attribute + funcationality class

class Device:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    
    def coding(self):
        return f'learning python and practicing'
    
class Phone(Device):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f'sending SMS to: {number} with {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.dual_sim}, {self.brand}, {self.color}, {self.origin}, {self.price}'
    
class camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass


#inheritance

my_phone = Phone('iphone', 120000, 'silver', 'china', True)
print(my_phone)
