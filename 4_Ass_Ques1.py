def balanced_string(s):
    newString = []
    count_L = 0
    count_R = 0
    currentString =""

    for char in s:
        currentString +=char


        if char == 'L':
            count_L += 1
        if char == 'R':
            count_R += 1
        
        if count_R == count_L:
            newString.append(currentString)
            currentString = ""
            count_L = 0
            count_R = 0
    
    return newString


s1 = input()
result = balanced_string(s1)
print(len(result))
print("\n".join(result))
    