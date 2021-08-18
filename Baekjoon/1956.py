# Baekjoon - 1956 (pypy3)
import sys
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
dist = [[INF]*V for _ in range(V)]
answer = INF

for _ in range(E): 
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    
# Floyd - Warshall
for k in range(V):
    for i in range(V):
        for j in range(V):
            #dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(V):
    answer = min(answer, dist[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)