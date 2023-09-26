a = [0]*5
a[:] = map(int, input().split())

#1번
c = a[0]**2+a[1]**2+a[2]**2+a[3]**2+a[4]**2
c = c % 10
print(c)