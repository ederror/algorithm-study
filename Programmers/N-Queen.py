# Programmers - N-Queen
answer = 0

def func(queen, row, n):
    global answer
    if row == n: # 재귀호출 종료조건
        answer += 1
        return
    
    for c in range(n): # [row, c]에 새로운 말을 놓을 수 있는지 확인
        flag = 0
        for q in queen: # 이전 말들 확인
            if q[1] == c or abs(q[0]-row) == abs(q[1]-c):
                flag = 1
                break
        
        if flag == 0: # 이전 말들이 공격할 수 없는 위치라면
            queen.append([row,c])
            func(queen, row+1, n)
            queen.pop()
    
def solution(n):
    
    for c in range(n):
        func([[0, c]], 1, n)
        
    return answer