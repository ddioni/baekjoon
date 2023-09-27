def switch(a, b, t):
    c = t[a-1]
    t[a-1] = t[b-1]
    t[b-1] = c
    return t
    
n, m = map(int, input().split())
t = []

for i in range(n):
    t.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    t = switch(a, b, t)

for i in range(n):
    print(t[i], end=" ")