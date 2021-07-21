# Programmers - 최고의 집합
def solution(n, s):
    if s < n: # Exception
        return [-1]
    
    remainder = s % n
    answer = [s//n] * n
    
    for i in range(n-1, n-remainder-1, -1):
        answer[i] += 1

    return answer