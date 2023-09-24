n, x = map(int, input().split())
a = [0]*(n-1)
a[:n-1] = map(int, input().split())

for i in a:
    if i < x:
        print(i, end=" ")