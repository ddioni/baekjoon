def group_check():
    s = input()
    a = []

    for i in range(len(s)):
        if s[i] in a:
            if s[i-1] == s[i]:
                continue
            else:
                return 0
        a.append(s[i])
    return 1

n = int(input())
sum = 0
for k in range(n):
    sum = sum + group_check()

print(sum)
