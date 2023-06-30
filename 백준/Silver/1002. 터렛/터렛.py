def turret():
    x1, x2, r1, y1, y2, r2 = map(int, input().split())
    distance = ((x1-y1)**2+(x2-y2)**2)**(1/2)
    if x1 == y1 and x2 == y2 and r1 == r2 == 0:
        print("1")
    elif x1 == y1 and x2 == y2 and r1 == r2 != 0:
        print("-1")
    elif x1 == y1 and x2 == y2 and r1 != r2:
        print("0")
    else:
        if distance == r1 + r2 or distance + min(r1, r2) == max(r1, r2):
            print("1")
        elif abs(r1 - r2) < distance < r1 + r2 :
            print("2")
        else:
            print("0")
        

number = int(input())
for i in range(number):
    turret()
