# Baekjoon - 2252
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

edges = {i: [] for i in range(1,N+1)}
indegree = [0]*(N+1)
for __ in range(M):
    a, b = map(int ,input().split())
    if a != b:
        edges[a].append(b)
        indegree[b] += 1

queue = deque([])
for v in range(1, N+1):
    if indegree[v] == 0:
        queue.append(v)

answer = []
while queue:
    v = queue.popleft()
    answer.append(v)

    for w in edges[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            queue.append(w)
print(*answer)