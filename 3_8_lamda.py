# lamda

def doubled(x):
    return x*2


result = doubled(44)
print(result)

doubled = lambda num : num*2
squared = lambda num : num*num


result = doubled(44)
output = squared(9)

add = lambda x,y : x+y
add(50, 60)
print(result, output, add)

numbers = [12,56,58,25,60]

doubled_nums = map(doubled, numbers)
print(numbers)
print(list(doubled_nums))

squared_nums = map(lambda x: x*x, numbers)
print(list(squared_nums))

actors = [
    {'name' : 'sabana', 'age': 65},
    { 'name' : 'sabnoor', 'age' : 23}
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
print(list(juniors))