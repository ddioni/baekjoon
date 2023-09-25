n = int(input())
count = 0

k = n #temporal n

while True:
    if k < 10:
        a = k #a는 양쪽 자리 더 한 수
        k = k * 11
    else:
        a = k // 10 + k % 10
        k = k % 10 * 10 + a % 10
        
    count = count + 1
    
    if k == n:
        break
    
print(count) 