zerod = [0] * 50
oned = [0] * 50
def fibonacci(n):
    if n == 0:
        zerosum = 1
        onesum = 0
        return zerosum, onesum

    elif n == 1:
        onesum = 1
        zerosum = 0
        return zerosum, onesum

    else:
        if zerod[n] != 0 or oned[n] != 0:
            return zerod[n], oned[n]
        else:    
            zerosum1, onesum1 = fibonacci(n-1)
            zerosum2, onesum2 = fibonacci(n-2)
            zerosum = zerosum1 + zerosum2
            onesum = onesum1 + onesum2
            zerod[n] = zerosum
            oned[n] = onesum
        return zerod[n], oned[n]


def number():
    n = int(input())
    a = []
    for i in range(n):
        b = int(input())
        a.append(b)

    for j in a:
        zerosum, onesum = fibonacci(j)
        print(zerosum, onesum)

number()