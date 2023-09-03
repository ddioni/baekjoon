import sys
input = sys.stdin.readline

def stack():
    n = int(input())
    s = []
    for i in range(n):
        k = input()

        if k[0:2] == "pu":
            s.append(int(k[5:]))
        elif k[0:2] == "po":
            if len(s) != 0:
                m = s.pop(len(s)-1)
                print(m)
            else:
                print("-1")
        elif k[0:2] == "si":
            m = len(s)
            print(m)
        elif k[0:2] == "em":
            if len(s) == 0:
                print("1")
            else:
                print("0")
        elif k[0:2] == "to":
            if len(s) != 0:
                print(s[len(s)-1])
            else:
                print("-1")

stack()
