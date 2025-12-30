test = int(input())
count = 0

for _ in range(test):
    nums = list(map(int, input().split()))
    if sum(nums) >= 2:
        count += 1
print(count)