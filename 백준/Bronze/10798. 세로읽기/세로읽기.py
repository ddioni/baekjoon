a = []
len_a = []
for i in range(5):
    s = list(input())
    a.append(s)
    len_a.append(len(s))

for j in range(max(len_a)):
    for i in range(5):
        try:
            print(a[i][j], end="")
        except:
            continue