def print_Left_To_Right(num):
    digit = str(num)
    print(" ".join(digit[::-1]))


T = int(input())

for _ in range (T):
    N = int(input())
    print_Left_To_Right(N)
