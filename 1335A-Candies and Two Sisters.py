test = int(input())
ans = []

for _ in range(test):
    num = int(input())

    divided = (num -1) //2
    if divided == 0:
        ans.append(0)
    else:
        ans.append(divided)


for num in ans:
    print(num)