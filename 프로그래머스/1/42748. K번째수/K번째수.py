def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        
        temp = sorted(array[i-1:j])
        
        print(temp, k)
        answer.append(temp[k-1])
        
        
    return answer