n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)
    
p = list(s[0])
for k in s[1:]:
    for j in range(len(k)):
        if p[j] != k[j] and p[j] != "?":
            p[j] = "?"
        else:
            continue
print(''.join(p))
