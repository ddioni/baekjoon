import math

def bridge():
    m, n = map(int, input().split())
    k = n - m

    if k == 0:
        print(1)
    else:
        print(math.factorial(n)//(math.factorial(m)*math.factorial(k)))

n = int(input())
for i in range(n):
    bridge()