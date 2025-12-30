test = int(input())
arr= []

for _ in range(test):
    a, b = list(map(int, input().split()))
    move = (b - (a % b)) % b
    arr.append(move)
for num in arr:
    print(num)