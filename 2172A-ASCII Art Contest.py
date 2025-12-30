scores = list(map(int, input().split(" ")))

if max(scores) - min(scores) >= 10:
    print("check again")
else:
    scores.sort()
    n = len(scores)
    median = scores[n//2]
    print("final", median)