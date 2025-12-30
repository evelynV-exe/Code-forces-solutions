test = int(input())

for _ in range(test):
    num = input()
    digitS =0
    for d in num:
        digitS += int(d)
    print(digitS)