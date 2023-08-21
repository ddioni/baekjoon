def sugar_box(n):
    num = 0
    
    while n >= 5:
        if n % 5 == 0:
            num = num + n // 5
            return num
        else:
            n = n - 3
            num = num + 1

            
    if n == 4 or n == 2 or n == 1:
        return -1
    
    if n == 3:
        num = num + 1
        return num
 
n = int(input())
num = sugar_box(n)
print(num)
