def frequencyArray(N, M, A):
    freq_dictonary = {}

    for num in A:
        freq_dictonary[num] = freq_dictonary.get(num,0) + 1

    result = [freq_dictonary.get(i, 0) for i in range(1, M+1)]
    return result



N, M = map(int, input().split())
A =list(map(int, input().split()))
result = frequencyArray(N, M, A)

for value in result:
    print(value)
