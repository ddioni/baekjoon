N, B = map(int, input().split())
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
new = []

while N != 0:
    n = N % B
    N = N // B
    if n in number:
        i = number.index(n)
        new.append(alpha[i])
    else:
        new.append(str(n))
new.reverse()
print(''.join(new))