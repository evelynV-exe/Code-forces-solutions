import string
numChar = int(input())
strInput = input()

for letter in string.ascii_lowercase:
    if strInput.lower().count(letter) == 0:
        print("NO")
        break
else:
    print("YES")