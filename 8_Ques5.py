import time

def timer(func):
    def inner():
        print('Time started')
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Time ended. Execution time: {end_time - start_time:.4f} seconds')
    return inner

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f'Factorial of {num} is {result}')

timed_factorial = timer(factorial)
timed_factorial(5)
