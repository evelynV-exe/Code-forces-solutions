n = int(input())
capa = 0
maxCapa = 0

for _ in range(n):
    exit, enter = list(map(int, input().split()))

    capa -= exit
    capa += enter

    if capa > maxCapa:
        maxCapa = capa

print(maxCapa)