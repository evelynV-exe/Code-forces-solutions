nums = list(map(int, input().split()))
nums.sort()

#max
s = nums[3]
a = s - nums[2]
b = s - nums[1]
c = s - nums[0]
print(a, b, c)