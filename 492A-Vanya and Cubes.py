n = int(input())

h = 0
used = 0

while True:
    nextL = (h + 1) * (h + 2) // 2
    if used + nextL > n:
        break
    used += nextL
    h += 1

print(h)