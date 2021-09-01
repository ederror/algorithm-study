# Programmers - 이중우선순위큐
def solution(operations):
    q = []
    answer = [0, 0]
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            q.append(int(num))
            q.sort()
        else: # 'D'
            if not q:
                continue
            if num == '1': # 최댓값 삭제
                q.pop()
            else:
                q.pop(0)
    if q:
        answer = [q[-1], q[0]]
    return answer