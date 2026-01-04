n = int(input())
crime = list(map(int, input().split()))
total = 0
count = 0

for num in crime:
    if num > 0:
        total += num
    else:
        if total > 0:
            total -= 1
        else:
            count += 1

print(count)
