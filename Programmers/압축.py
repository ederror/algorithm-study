# Programmers - 압축
def solution(msg):
    answer = []
    dictionary = {chr(ord('A')+i):i+1 for i in range(26)}
    idx = 27
    s = 0
    while s <= len(msg):
        i = 1
        while s + i <= len(msg) and msg[s:s+i] in dictionary:
            i += 1
        
        if msg[s:s+i] in dictionary:
            answer.append(dictionary[msg[s:s+i]])
            break
        
        answer.append(dictionary[msg[s:s+i-1]])
        dictionary[msg[s:s+i]] = idx
        idx += 1
        s = s+i-1
        
    return answer