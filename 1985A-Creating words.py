test = int(input())
arr = []

for _ in range(test):
    word = input().split()
    a = word[0]
    b = word[1]

    aSwap = b[0] + a[1:3]
    bSwap = a[0] + b[1:3]
    arr.append((aSwap, bSwap))

for aSwap, bSwap in arr:
    print(aSwap, bSwap)