def change(a, i, j):
    l = j - i
    for m in range(l//2+1):
        t = a[i+m]
        a[i+m] = a[j-m]
        a[j-m] = t
    return a
        

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(i+1)
    
for k in range(m):
    i, j = map(int, input().split())
    a = change(a, i-1, j-1)

for i in range(n):
    print(a[i], end=" ")
