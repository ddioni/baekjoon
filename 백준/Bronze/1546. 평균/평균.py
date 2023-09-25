n = int(input())
a = [0]*n
a[:] = map(int, input().split())
m = max(a)

for i in range(n):
    a[i] = a[i]/m*100
print(sum(a)/len(a))