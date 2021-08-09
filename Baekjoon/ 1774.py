# Baekjoon - 1774
import sys
import math
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

answer = 0
N, M = map(int, input().split())
node = []
parent = [i for i in range(N)]
edge = []
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    node.append([x, y])
    
for _ in range(M):
    v, w = map(int, input().split())
    if find(v-1) != find(w-1):
        union(v-1, w-1)
        cnt += 1

for i in range(N):
    for j in range(i+1, N):
        weight = math.sqrt( ((node[i][0] - node[j][0]) ** 2)+((node[i][1] - node[j][1]) ** 2) )
        edge.append([i, j, weight])
        
edge.sort(key = lambda x : x[2])

# Kruskal's Algorithm
while cnt < N-1: # edge를 N-1개 선택할 때까지 반복
    e = edge.pop(0)
    if find(e[0]) != find(e[1]):
        union(e[0], e[1])
        cnt += 1
        answer += e[2]
    
print(f'{answer:.2f}')