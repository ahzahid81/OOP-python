balance = 3000

def buy_thing(item, price):
    balance = 400
    balance = balance - price
    print('balance inside the function', balance)

buy_thing('sunglass', 1000)
print(balance)