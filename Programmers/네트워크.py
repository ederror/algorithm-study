# Programmers - 네트워크
def solution(n, computers):
    answer = 0
    visited = []
    
    for i in range(n):
        if i not in visited:
            # BFS - 노드 i가 속한 네트워크의 모든 노드 방문
            q = [i]
            visited.append(i)
            
            while q:
                v = q.pop(0)
                for w in range(n):
                    if computers[v][w] == 1 and w not in visited:
                        visited.append(w)
                        q.append(w)
                        
            answer += 1
    return answer