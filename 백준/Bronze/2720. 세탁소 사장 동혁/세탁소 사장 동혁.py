n = int(input())

for i in range(n):
    k = int(input())
    quarter = k // 25
    k = k % 25
    
    dime = k // 10
    k = k % 10

    nickel = k // 5
    k = k % 5

    penny = k

    print(quarter, dime, nickel, penny)
    
