a = []
n = int(input())
for i in range(n):
    k = int(input())
    a.append(k)
a.sort()

for i in range(n):
    print(a[i])
