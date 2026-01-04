friends = int(input())
gift = list(map(int, input().split()))

giver = [0] * friends

for i in range(friends):
    giver[gift[i] -1] = i + 1
print(*giver)