def solve():
    kilo = int(input())

    if kilo % 2 == 0 and kilo > 2:
        return "YES"
    else:
        return "NO"
    
print(solve())