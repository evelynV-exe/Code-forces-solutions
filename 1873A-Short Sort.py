test = int(input())
target = "abc"

for i in range(test):
    string = input().strip()
    diff = sum(1 for i in range(3) if string[i] != target[i])
    if diff == 0 or diff == 2:
        print("YES")
    else:print("NO")