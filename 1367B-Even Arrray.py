test = int(input())
arr = []

for _ in range(test):
    numArr = int(input())
    num = list(map(int, input().split()))
    moveEven = 0
    moveOdd = 0

    for i in range(numArr):
        if (i % 2) != (num[i] % 2):
            if i % 2 == 0:
                moveEven += 1
            else:
                moveOdd += 1

    arr.append((moveEven, moveOdd))

for moveEven, moveOdd in arr:
    if moveEven == moveOdd:
        print(moveEven)
    else:
        print(-1)