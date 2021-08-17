# Baekjoon - 11657
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int ,input().split())
dist = [INF for _ in range(N)]
dist[0] = 0
graph = [[] for _ in range(N)]
flag = 0

for _ in range(M):
    a, b, c = map(int ,input().split())
    graph[a-1].append([b-1, c])

for _ in range(N-1):
    for v in range(N):
        for w, cost in graph[v]:
            if dist[v] == INF:
                continue
            dist[w] = min(dist[w], dist[v] + cost)

# 음수 사이클 확인
for v in range(N):
    for w, cost in graph[v]:
        if dist[w] > dist[v] + cost:
            flag = 1

if flag:
    print(-1)
else:
    for d in dist[1:]:
        if d == INF:
            print(-1)
        else:
            print(d)
