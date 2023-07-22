def full_name(first, last):
    name = f'{first} {last}'
    return name

# take parameters in orders
name = full_name('Alu', 'kodu')
name = full_name(last= 'Zahid', first='Abdul' )
print(name)

def famous_name(first, last, title, additional):
    name = f'{title} {first} {last} {additional}'
    return name

name = famous_name('Taheri', 'Ali', 'bondo', 'hujur')
print(name)