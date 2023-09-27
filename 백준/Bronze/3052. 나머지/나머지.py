a = []
for i in range(10):
    k = int(input())
    a.append(k%42)
print(len(list(set(a))))