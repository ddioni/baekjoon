def prince():
    start_x, start_y, end_x, end_y = map(int, input().split())
    planet_num = int(input())
    count = 0
    start_end_distance = (start_x - end_x)**2 + (end_x - end_y)**2
    
    for i in range(planet_num):
        x, y, r = map(int, input().split())
        start_distance = (start_x - x)**2 + (start_y - y)**2
        end_distance = (end_x - x)**2 + (end_y - y)**2
        
        if start_distance < r**2 and end_distance < r**2:
            continue
        elif start_distance < r**2 or end_distance < r**2:
            count += 1
    print(count)

num = int(input())
for n in range(num):
    prince()