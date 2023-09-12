m, n = map(int, input().split())
a = []
b = []

for i in range(m):
    j = map(int, input().split())
    a.append(list(j))

for i in range(m):
    k = map(int, input().split())
    b.append(list(k))

for i in range(m):
    for j in range(n):
        s = a[i][j] + b[i][j]
        if j == n-1:
            print(s)
        else:
            print(s, end=" ")