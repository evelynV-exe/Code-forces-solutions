n = int(input())
result = []

for _ in range(n):
    string = input()
    if len(string) > 10:
        word = string[0] + str(len(string) - 2) + string[-1]
    else:
        word = string

    result.append(word)

for word in result:
    print(word)