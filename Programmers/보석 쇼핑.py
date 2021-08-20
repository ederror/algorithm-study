# Programmers - 보석 쇼핑
def solution(gems):
    answer = [-1, len(gems)]
    N = len(set(gems))
    s, e = 0, 0
    gemsDict = {}
    gemsDict[gems[0]] = 1
    
    while s <= e and e < len(gems):
        
        if len(gemsDict) < N:
            if e == len(gems)-1: 
                break
            e += 1
            if gems[e] not in gemsDict:
                gemsDict[gems[e]] = 1
            else:
                gemsDict[gems[e]] += 1
        else: 
            if answer[1] - answer[0] > e - s:
                answer = s+1, e+1
                
            if gemsDict[gems[s]] == 1:
                del gemsDict[gems[s]]
            else:
                gemsDict[gems[s]] -= 1
            s += 1
        
    return answer