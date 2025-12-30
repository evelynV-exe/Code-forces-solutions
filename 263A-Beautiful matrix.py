r = c = None
for i in range(5):
    num = list(map(int, input().split()))
    for j in range(5):
        if num[j] == 1:
            r, c = i+1, j+1

if r is not None and c is not None:
    print(abs(r-3) + abs(c - 3))