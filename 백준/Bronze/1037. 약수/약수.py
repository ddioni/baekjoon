n = int(input())
a = list(map(int, input().split()))

if len(a) == 1:
    print(a[0]**2)
else:
    print(max(a)*min(a))