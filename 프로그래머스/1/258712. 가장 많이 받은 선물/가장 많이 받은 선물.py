def compare(m, n):
    if m > n:
        return 1
    elif m == n:
        return 0
    else:
        return -1

def put(d, key, value):
    if key in d.keys():
        d[key] += value
    else:
        d[key] = value

def solution(friends, gifts):
    answer = 0
    
    give = []
    get = []
    
    total = {}
    result = {}
    point = {}
    
    #전체 기프트 수 카운트
    for gift in gifts:
        a, b = gift.split()
        
        give.append(a)
        get.append(b)
        put(total, gift, 1)
        
    #각 이름별 포인트 계산 및 가능한 조합 구성
    combination = []
    for i in range(len(friends)):
        friend = friends[i]
        n = give.count(friend) - get.count(friend)
        point[friend] = n
        for j in range(i+1, len(friends)):
            combination.append(friend+" "+friends[j])
            combination.append(friends[j]+" "+friend)
    
    #선물 주고받은 애들끼리 비교
    checked = []
    for item in total.items():
        a, b = item[0].split()
        n = item[1]
        
        if item[0] in checked:
            continue
        
        s = b+" "+a
        if s in total.keys():
            r_n = total[s]
            if compare(n, r_n) == 1: #n이 더 큼 -> a가 선물 더 많이 줌
                put(result, a, 1)
                
            elif compare(n, r_n) == 0: #같으면 지수 비교
                if point[a] > point[b]:
                    put(result, a, 1)
                elif point[a] < point[b]:
                    put(result, b, 1)
                        
            else:
                put(result, b, 1)
                
            
        else:
            put(result, a, 1)
            
        checked.append(s)
        combination.remove(s)
        combination.remove(item[0])
        #print(a, b, result)    
    
    #선물 안 주고받은 애들끼리 비교
    checked_comb = []
    for comb in combination:
        if comb in checked_comb:
            continue
        
        a, b = comb.split()
        if point[a] > point[b]:
            put(result, a, 1)
        elif point[a] < point[b]:
            put(result, b, 1)
        checked_comb.append(b+" "+a)
    
    print(result)
    answer = max(result.values()) if len(result) > 0 else 0
    return answer