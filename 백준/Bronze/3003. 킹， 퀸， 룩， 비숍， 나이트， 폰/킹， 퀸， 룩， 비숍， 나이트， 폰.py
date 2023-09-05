a = []*6
a[0:6] = map(int, input().split())

for i in range(len(a)):
    if i == 0 or i == 1:
        a[i] = 1 - a[i]
    elif i == 2 or i == 3 or i == 4:
        a[i] = 2 - a[i]
    elif i == 5:
        a[i] = 8 - a[i]

print(a[0], a[1], a[2], a[3], a[4], a[5])