alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

s = input()
t = 0

for i in s:
    t += number[alphabet.index(i)]+1
print(t)
