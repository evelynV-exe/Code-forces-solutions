limak, bob = list(map(int, input().split()))
weight = True
count = 0

while weight:
    if limak <= bob:
        limak *= 3
        bob *= 2
        count += 1
    else:
        weight = False
    
print(count)