test = int(input())
ans = []

for _ in range(test):
    nums = list(map(int, input().split()))
    nums.sort()
    ans.append(nums[1])

for num in ans:
    print(num)