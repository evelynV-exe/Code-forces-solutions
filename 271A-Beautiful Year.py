year = int(input())

while True:
    year += 1
    digits = str(year)
    if len(digits) == len(set(digits)):
        print(year)
        break