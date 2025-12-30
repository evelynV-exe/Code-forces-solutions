test = int(input())

for _ in range(test):
    num = list(map(int, input().split()))

    num.sort()
    
    if num[0] + num[1] == num[2]:
        print("YES")
    else:
        print("NO")