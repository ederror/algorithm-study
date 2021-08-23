# Programmers - 뉴스 클러스터링
def solution(str1, str2):
    def parse(string):
        res = []
        string = string.lower()
        
        for i in range(len(string) - 1):
            buffer = string[i:i+2]
            if not(ord('a')<=ord(buffer[0])<=ord('z')):
                continue
            if not(ord('a')<=ord(buffer[1])<=ord('z')):
                continue
            res.append(buffer)    
        return res
               
    answer = 0
    mul1, mul2 = parse(str1) , parse(str2)
    
    len_union = len(mul1)+len(mul2)
    len_inter = 0
    
    for e in mul1:
        try:
            idx = mul2.index(e)
            len_inter += 1
            del mul2[idx]
        except:
            continue
            
    len_union -= len_inter
    
    if len_union == 0:
        answer = 1
    else:
        answer = (len_inter / len_union)
    answer = answer * 65536 * 10 // 10

    return answer