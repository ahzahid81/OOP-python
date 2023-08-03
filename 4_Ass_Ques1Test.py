def split_balanced_string(s):
    balanced_strings = []
    count_L = 0
    count_R = 0
    current_string = ""

    for char in s:
        current_string += char
        if char == 'L':
            count_L += 1
        else:
            count_R += 1

        if count_L == count_R:
            balanced_strings.append(current_string)
            current_string = ""
            count_L = 0
            count_R = 0

    return balanced_strings


# Test cases
s1 = "LLRRLLLRRR"
result1 = split_balanced_string(s1)
print(len(result1))
print("\n".join(result1))

s2 = "LLLRRR"
result2 = split_balanced_string(s2)
print(len(result2))
print("\n".join(result2))
