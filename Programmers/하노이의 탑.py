# Programmers - 하노이의 탑
answer = []
def moveDisk(s, e, n): # s -> e 로 n개의 원판을 옮김
    global answer
    if n == 1: # 종료조건
        answer.append([s,e])
        return
    
    m = 6 - s - e # 중간에 거치는 곳
    
    # n-1개 원판을 s->m
    moveDisk(s, m, n-1)
    # n-1번째 원판 s->e
    answer.append([s,e])
    # 다시 n-1개 원판을 m->e
    moveDisk(m, e, n-1)
    
def solution(n):
    moveDisk(1, 3, n)
    return answer