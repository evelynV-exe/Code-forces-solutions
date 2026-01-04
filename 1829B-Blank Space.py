test = int(input())

for _ in range(test):
    num = int(input())
    numlist = input().split()
    count = 0
    best = 0

    for n in numlist:
        if n == "0":
            count += 1
            best = max(best, count)
        else:
            count = 0
    print(best)