# Programmers - 합승 택시 요금
import heapq
from collections import defaultdict
def solution(n, s, a, b, fares):
    
    def dijkstra(v):
        dist = [float('inf')]*(n+1)
        dist[v] = 0
        s = [] # 아직 체크 안 한
        heapq.heappush(s, [0, v])
        while s:
            # s에 있는 노드 중 dist값이 최소인 노드 찾음
            curdist, v = heapq.heappop(s)
            if v not in graph:
                continue
            for w, cost in graph[v]:
                if dist[w] > dist[v] + cost:
                    dist[w] = dist[v] + cost
                    heapq.heappush(s, [dist[v]+cost, w])
        return dist
        
    answer = float('inf')
    graph = defaultdict(list)
    for v,w,cost in fares:
        graph[v].append([w, cost])
        graph[w].append([v, cost])
    
    distance = []
    for v in range(n+1): # dijkstra table 만들기
        distance.append(dijkstra(v))
    
    for m in range(1,n+1): # 노드 m까지 합승 s->m + m->a + m->b
        if answer > distance[s][m] + distance[m][a] + distance[m][b]:
            answer = distance[s][m] + distance[m][a] + distance[m][b]
            
    return answer