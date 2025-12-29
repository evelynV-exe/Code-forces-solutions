def solve():
    # number of arrays
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        currentMax= 0
        removals = 0

        for x in a:
            if x < currentMax:
                removals += 1
            else:
                currentMax = x

        results.append(removals)
    return results

results = solve()
for ans in results:
    print(ans)
