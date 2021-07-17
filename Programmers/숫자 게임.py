# Programmers - 숫자 게임
def solution(A, B):
    answer = 0
    N = len(A)
    A.sort()
    B.sort()
    
    i = 0
    for a in A:
        while i < N and a >= B[i]:
            i += 1
        if i < N and a < B[i]:
            answer += 1
            i += 1
    
    return answer