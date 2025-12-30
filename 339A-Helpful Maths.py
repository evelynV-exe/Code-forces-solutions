string = list(map(int, input().replace("+", "")))
string.sort()
ans = '+'.join(str(num) for num in string)

print(ans)