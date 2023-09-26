a = []
for i in range(28):
    n = int(input())
    a.append(n)


for i in range(1, 31):
    if i not in a:
        print(i)