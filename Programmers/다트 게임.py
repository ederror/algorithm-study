# Programmers - 다트 게임
def solution(dartResult):
    score = []
    buf = ""
    for c in dartResult:
        if ord('0')<= ord(c) <=ord('9'):
            buf += c
        else:
            if buf != "":
                score.append(int(buf))
                buf = ""
            
            if c == '*':
                score[-1] *= 2
                if len(score) > 1:
                    score[-2] *= 2
            elif c == '#':
                score[-1] *= -1
            elif c == 'D':
                score[-1] = score[-1] ** 2
            elif c == 'T':
                score[-1] = score[-1] ** 3    
    
    return sum(score)