n, m = map(int, input().split())
a = []
yes_X_n = []
for i in range(n):
    k = list(input())
    a.append(k)
    for j in range(m):
        if k[j] == "X" and j not in yes_X_n:
            yes_X_n.append(j) #여기에 없으면 X 추가 필요

yes_X_m = []
b = list(zip(*a))
for i in range(m):
    for j in range(n):
        if b[i][j] == "X" and j not in yes_X_m:
            yes_X_m.append(j)

sum1 = m-len(yes_X_n)
sum2 = n-len(yes_X_m)
x = 0
while True:
    if sum1 == 0 or sum2 == 0:
        break
    sum1 = sum1 - 1
    sum2 = sum2 - 1
    x = x + 1
    
print(sum1+sum2+x)