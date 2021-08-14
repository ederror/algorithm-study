# Baekjoon - 9370
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(v): # v로부터 모든 노드까지의 최단거리 반환
    dist = [graph[v][i] for i in range(n)]
    dist[v] = 0
    Q = [i for i in range(n)]
    Q.pop(v)
    
    while Q:
        minDist, u = INF, -1
        for q in Q:
            if dist[q] <= minDist:
                minDist, u = dist[q], q
        Q.remove(u)
        
        for i in range(n):
            if dist[i] > dist[u] + graph[u][i]:
                dist[i] = dist[u] + graph[u][i]
    return dist
    
    
T = int(input())
for tc in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split()) # s 는 출발점 / g-h를 반드시 지남
    
    graph = [[INF]*n for _ in range(n)]
    targets = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a-1][b-1] = d
        graph[b-1][a-1] = d
    
    dist_s = dijkstra(s-1)
    dist_g = dijkstra(g-1)
    dist_h = dijkstra(h-1)
   
    for _ in range(t):
        target = int(input())
        if dist_s[target-1] == (dist_s[g-1] + graph[g-1][h-1] + dist_h[target-1]):
            targets.append(target)
        elif dist_s[target-1] == (dist_s[h-1] + graph[h-1][g-1] + dist_g[target-1]):
            targets.append(target)
    
    targets.sort()
    print(*targets)
        
        
    