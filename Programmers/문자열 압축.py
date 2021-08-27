# Programmers - 문자열 압축
def solution(s):
    answer = len(s)
    for unit in range(1, len(s)):
        prev = s[0:unit]
        cnt = 1
        length = len(s)
        for i in range(unit, len(s), unit):
            if i+unit > len(s):
                break
                
            if prev == s[i: i+unit]:
                cnt += 1
                length -= unit
            else:
                if cnt != 1:
                    length += len(str(cnt))
                prev = s[i:i+unit]
                cnt = 1
                
        if cnt != 1:
            length += len(str(cnt))
            
        answer = min(answer, length)
    return answer