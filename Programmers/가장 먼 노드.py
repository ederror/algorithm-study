# Programmers - 가장 먼 노드
def solution(n, edge):
    answer = 0

    # edge 정보 -> graph 2차원 배열
    # (인접 노드 탐색시 모든 edge 탐색하는 것 보다 graph 배열 사용하는 것이 효율적)
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    

    # dist : 0이면 아직 방문X, 노드 1부터 최단거리 저장
    dist = [0 for _ in range(n+1)]

    q = [1] # queue for BFS
    dist[1] = 1 #1번노드 방문표시 
    
    # BFS
    while q:
        v = q.pop(0)
        for w in graph[v]:
            if dist[w] == 0:
                dist[w] = dist[v] + 1
                q.append(w)
    
    # 가장 먼 노드 개수 구하기
    maxDist = max(dist)
    for d in dist:
        if d == maxDist:
            answer += 1
    return answer