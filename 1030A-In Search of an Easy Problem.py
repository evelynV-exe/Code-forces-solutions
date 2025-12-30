people = int(input())
opinions = list(map(int, input().split()))
count = 0

if people == 1 and 0 in opinions:
    print("EASY")
else:
    if 1 in opinions:print("HARD")
    else:print("EASY")