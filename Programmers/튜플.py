# Programmers - 튜플
def solution(s):
    answer = []
    s_splited = []
    for str in s[2:-2].split("},{"):
        s_splited.append(set(map(int, str.split(","))))
    
    s_splited.sort(key = lambda x : len(x))

    prevSet = set([])
    for curSet in s_splited:
        diff = list(curSet - prevSet)
        prevSet = curSet
        answer.append(diff[0])
            
    return answer