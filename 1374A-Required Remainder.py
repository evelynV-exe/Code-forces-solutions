test = int(input())
arr = []

for _ in range(test):
    x, y, n = list(map(int, input().split()))
    
    if (n - n % x + y <= n):
        num = n- n % x + y
    else:
        num = n- n % x - (x - y)
    arr.append(num)

for num in arr:
    print(num)