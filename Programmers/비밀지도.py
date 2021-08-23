# Programmers - 비밀지도
def solution(n, arr1, arr2):
    answer = []
    bi = [2**i for i in range(n-1, -1, -1)]
    
    for i in range(n):
        buf = ""
        for b in bi:
            if arr1[i] >= b or arr2[i] >= b:
                buf += "#"
                if arr1[i] >= b:
                    arr1[i] -= b
                if arr2[i] >= b:
                    arr2[i] -= b
            else:
                buf += " "
        answer.append(buf)
        
    return answer