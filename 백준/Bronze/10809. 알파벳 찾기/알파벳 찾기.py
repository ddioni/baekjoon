a = [-1]*26
s = input()

for i in range(len(s)):
    k = ord(s[i])-97
    if a[k] == -1:
        a[k] = i
    else:
        continue

for i in a:
    print(i, end=" ")