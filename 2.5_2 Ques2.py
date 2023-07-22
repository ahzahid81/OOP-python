import sys


def sum_odd_numbers_between(x,y):
    if x>y:
        x, y = y, x

    total_sum = 0

    for num in range(x+1, y):
        if(num%2 !=0):
            total_sum+=num

    return total_sum


T = int(input())
if T<1 or T>10:
    sys.exit()


for _ in range(T):
    X, Y = map(int, input().split())
    result = sum_odd_numbers_between(X, Y)
    print(result)

