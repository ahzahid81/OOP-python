class Shopping:
    cart = [] #class attribute #static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = 'Jamu na City' # instance Attribute
        self.location = 'Jam er maj Khane'

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def mulitipy( a, b):
        result = a*b
        print(result)
    

    @classmethod
    def hudai_dekhi(self, item):
        print('hudai dekhi kintu kinmu na just ac ar hawa khaite aschi', item)



basundara = Shopping('basundara', 'dhaka')
# basundara.purchase('lungi', 500, 1000)
basundara.hudai_dekhi('lungi')
Shopping.hudai_dekhi('lungi') 
Shopping.mulitipy(4,6) #static method

