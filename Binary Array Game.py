t = int(input())

for _ in range(t):
    a = int(input())
    num = list(map(int, input().split()))

    if num[0] == 0 and num[-1] == 0:
        print("Bob")
    else:
        print("Alice")
