def check(a):
    operation = 0
    while all(x%2==0 for x in a):
        a = [x//2 for x in a]
        operation += 1
    return operation



N = int(input())
a = []

a.extend(map(int, input().split()))

result = check(a)
print(result)