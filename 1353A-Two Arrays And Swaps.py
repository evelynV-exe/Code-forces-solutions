test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    for i in range(min(n, k)):
        if b[i] > a[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    print(sum(a))