import sys
input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s_t = a[0]*b[1]+b[0]*a[1]
s_b = a[1]*b[1]
n = gcd(s_t, s_b)
s_t = s_t // n
s_b = s_b // n

print(s_t, s_b)