n=int(input())
for i in range(n):
    k, s = input().split()
    k = int(k)

    for i in s:
        print(i*k, end="")
    print()