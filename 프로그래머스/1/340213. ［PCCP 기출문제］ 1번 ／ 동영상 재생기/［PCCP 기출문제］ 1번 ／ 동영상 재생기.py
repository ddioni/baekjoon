def to_string(time):
    mm = time // 60
    ss = time % 60
    
    stringm = str(mm).zfill(2)
    strings = str(ss).zfill(2)
    
    return stringm+":"+strings
    
def compare(start, pos, end):
    if start <= pos <= end: 
        return end
    else: 
        return pos

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    vmm, vss = map(int, video_len.split(":"))
    videolen = vmm * 60 + vss
    
    smm, sss = map(int, op_start.split(":"))
    pmm, pss = map(int, pos.split(":"))
    emm, ess = map(int, op_end.split(":"))
    
    start = smm * 60 + sss
    intpos = pmm * 60 + pss
    end = emm * 60 + ess
    
    temp = compare(start, intpos, end)
    
    for command in commands:
        if command == "prev":
            if temp < 10:
                temp = 0
            else:
                temp -= 10
        elif command == "next":
            if temp > videolen - 10:
                temp = videolen
            else:
                temp += 10
        temp = compare(start,temp,end)
            
    answer = to_string(temp)
    return answer