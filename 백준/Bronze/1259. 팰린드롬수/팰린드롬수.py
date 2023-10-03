while True:
    n = input()
    flag = 0
    if n == "0":
        break

    for i in range(len(n)//2+1):
        if n[i] == n[len(n)-i-1]:
            continue
        else:
            print("no")
            flag = 1
            break
    if flag == 1:
        continue
    else:
        print("yes")