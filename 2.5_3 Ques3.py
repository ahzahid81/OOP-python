def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)



T = int(input())

numA = []

for i in range(T):
    result = str(fibonacci(i))

print(" ".join(result))