def check_VPS(a):
    left_num = 0
    valid_right_num = 0
    real_right_num = 0
    
    for i in a:
        if i == '(':
            left_num = left_num + 1
        elif i == ')':
            if left_num > valid_right_num:
                real_right_num = real_right_num + 1
                valid_right_num = valid_right_num + 1
            else:
                real_right_num = real_right_num + 1

    if left_num == valid_right_num == real_right_num:
        print("YES")
    else:
        print("NO")


n = int(input())
for j in range(n):
    a = input()
    check_VPS(a)