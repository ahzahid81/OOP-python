class shop:
    shopping_mall = 'jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)



mehzabeen = shop('meh jabeeeen')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = shop('noishp')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)