def solve():
    string = input()
    upperC = 0
    lowerC = 0


    for char in range(len(string)):
        if string[char].isupper():
            upperC += 1
        else:
            lowerC += 1

    if upperC > lowerC:
        return string.upper()
    else:
        return string.lower()

print(solve())