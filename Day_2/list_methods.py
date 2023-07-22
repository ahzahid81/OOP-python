numbers = [12,45,98,68]
numbers.append(56)
print(numbers)
numbers.insert(2, 71)
print(numbers)
numbers.remove(98)
print(numbers)
if 8 in numbers:
    numbers.remove(8)

numbers.pop()
print(numbers)
index = numbers.index(12)
print(index)
if 98 in numbers:
    index = numbers.index(98)
    print(index)

sorte = numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)