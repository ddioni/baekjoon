while True:
    name, age, weight = input().split()
    age, weight = int(age), int(weight)

    if name == "#":
        break

    if age > 17 or weight >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")