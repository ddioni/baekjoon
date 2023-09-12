def alpha_to_float(grade):
    if grade == "A+":
        return 4.5
    elif grade == "A0":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B0":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C0":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D0":
        return 1.0
    elif grade == "F":
        return 0.0

points = 0
sum = 0

for i in range(20):
    subject, point, grade = input().split()
    if grade == "P":
        continue
    point = float(point)
    grade = alpha_to_float(grade)
    total = point*grade
    sum = sum + total
    points = points + point

print(sum/points)