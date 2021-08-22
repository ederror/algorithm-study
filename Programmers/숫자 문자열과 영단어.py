# Programmers - 숫자 문자열과 영단어
def solution(s):
    answer = 0
    convert = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    i = 0
    while i < len(s):
        if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
            answer = answer*10 + ord(s[i])-ord('0')
            i += 1
        else:
            e = i
            while e < len(s) and s[i:e] not in convert:
                e += 1
            answer = answer*10 + convert[s[i:e]]
            i = e
    return answer