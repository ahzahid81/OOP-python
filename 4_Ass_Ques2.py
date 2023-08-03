def remove_occurance(a):
    freq_dictionary = {}

    for num in a:
        freq_dictionary[num] = freq_dictionary.get(num, 0) + 1

    removeOccurance = 0

    for num, freq in freq_dictionary.items():
        if freq > num:
            remove_occurance += freq-num

    return remove_occurance



N = int(input())
numbers = list(map(int, input().split()))

result = remove_occurance(numbers)
print(result)
