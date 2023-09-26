x = int(input())
a = []

while x > 1:
    a.append(x%2)
    x = x // 2
    
a.append(x)
count = 0
for i in a:
    if i == 1:
        count = count + 1
print(count)