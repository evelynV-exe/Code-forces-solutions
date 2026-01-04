n = int(input())
volume = list(map(int, input().split()))
total = 0

for num in volume:
    total += num * 0.01

result = (total/n) * 100
print(round(result, 12))