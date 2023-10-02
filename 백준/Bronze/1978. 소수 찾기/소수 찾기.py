n = int(input())
a = []
a[:] = map(int, input().split())
count = 0

for i in a:
    flag = 0
    if i == 1:
        continue
    elif i == 2:
        count = count + 1
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 1:
        continue
    count = count+1
    
print(count)