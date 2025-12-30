test = int(input())
arr = []

for _ in range(test):
    num = list(map(int, input().split()))
    arr.append(num)

for i in arr:
    if len(set(i)) == 1:
        print("YES")
    else:
        print("NO")