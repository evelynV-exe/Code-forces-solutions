t = int(input())

for _ in range(t):
    a, b, c, n = list(map(int, input().split()))

    total = a + b + c + n

    if total % 3 != 0:
        print("NO")
    else:
        x = total // 3
        if x >= max(a, b, c):
            print("YES")
        else:
            print("NO")