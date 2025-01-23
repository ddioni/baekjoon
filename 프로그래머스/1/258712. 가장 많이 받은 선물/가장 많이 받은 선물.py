
def solution(friends, gifts):
    
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    answer = [0]*l
    point = [0]*l
    gr = [[0] * l for i in range(l)]
    
    for gift in gifts:
        a, b = gift.split()
        gr[f[a]][f[b]] += 1
        point[f[a]] += 1
        point[f[b]] -= 1
    
    print(gr)
    print(point)
    
    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if point[i] > point[j]:
                    answer[i] += 1
            #print(answer)
            
    return max(answer)