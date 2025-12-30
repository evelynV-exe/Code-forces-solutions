num = int(input())
x = 0

for _ in range(num):
    operation = list(input())
    if operation[0] == '+' or operation[1] == '+':
        x +=1
    else:
        x -= 1
    
print(x)