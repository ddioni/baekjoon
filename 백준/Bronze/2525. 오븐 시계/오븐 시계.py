def oven_timer(h, m, cook):

    while cook >= 60:
        cook = cook - 60
        h = h + 1

        if h == 24:
            h = 0

    m = m + cook
    while m >= 60:
        m = m - 60
        h = h + 1

        if h == 24:
            h = 0

    print(str(h)+" "+str(m))

h, m = map(int, input().split())
cook = int(input())

oven_timer(h, m, cook)