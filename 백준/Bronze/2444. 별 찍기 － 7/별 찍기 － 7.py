n = int(input())

for i in range(1, 2*n):
    if i > n:
        i = 2*n - i
    print(" "*(n-i)+"*"*(2*i-1))