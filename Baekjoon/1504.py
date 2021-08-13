# Baekjoon - 1504
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(v): # 노드 v로부터 모든 정점까지의 최단거리를 구해 반환
    dist = [graph[v][i] for i in range(N)]
    dist[v] = 0
    Q = [i for i in range(N)]
    Q.pop(v)
    while Q:
        minValue, u = INF, -1
        for q in Q:
            if minValue >= dist[q]:
                minValue, u = dist[q], q
        Q.remove(u)
        
        for i in range(N):
            if dist[i] > dist[u] + graph[u][i]:
                dist[i] = dist[u] + graph[u][i]
    return dist    
    
N, E = map(int, input().split())
graph = [[INF]*N for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
   
v1, v2 = map(int, input().split())

dist_0 = dijkstra(0)
dist_v1 = dijkstra(v1-1)
dist_v2 = dijkstra(v2-1)

answer = INF
if answer > dist_0[v1-1] + dist_v1[v2-1] + dist_v2[N-1]:
    answer = dist_0[v1-1] + dist_v1[v2-1] + dist_v2[N-1]
if answer > dist_0[v2-1] + dist_v2[v1-1] + dist_v1[N-1]:
    answer = dist_0[v2-1] + dist_v2[v1-1] + dist_v1[N-1]
    
if answer < INF:
    print(answer)
else:
    print(-1)