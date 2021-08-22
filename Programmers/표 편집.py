# Programmers - 표 편집
def solution(n, k, cmd):
    answer = ""
    answer_list = ['O' for _ in range(n)]
    linkedList = {i: [i-1, i+1] for i in range(n)}
    linkedList[n-1][1] = -1
    
    cur = k # 현재 노드
    deleted = [] # 삭제된 노드 번호 저장
    
    for c in cmd:
        if c[0] == "U" or c[0] == "D": # 이동
            _, x = c.split()
            x = int(x)
            if c[0] == "U": # 왼쪽으로 x칸 이동
                for _ in range(x):
                    cur = linkedList[cur][0]
            else: # "D" - 오른쪽으로 x칸 이동
                for _ in range(x):
                    cur = linkedList[cur][1]
                    
        elif c[0] == "C": # 삭제
            deleted.append(cur)
            left, right = linkedList[cur]
            if left != -1:  # 왼쪽 노드의 오른쪽 포인터 수정
                linkedList[left][1] = right
                cur = left
            if right != -1: # 오른쪽 노드의 왼쪽 포인터 수정
                linkedList[right][0] = left
                cur = right 
                
        elif c[0] == "Z": # 복구
            restore = deleted.pop()
            left, right = linkedList[restore]
            if left != -1:  # 왼쪽 노드의 오른쪽 포인터 수정
                linkedList[left][1] = restore
            if right != -1: # 오른쪽 노드의 왼쪽 포인터 수정
                linkedList[right][0] = restore

    for d in deleted:
        answer_list[d] = 'X'
        
    answer = ''.join(answer_list)
    return answer