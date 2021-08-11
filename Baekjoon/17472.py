# Baekjoon - 17472
import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

N, M = map(int, input().split())
parent = [i for i in range(N*M)]
Map = []
islands = []
edges = []
for _ in range(N):
    Map.append(input().split())

for i in range(N):
    for j in range(M):
        if Map[i][j] == '1':
            if i > 0 and Map[i-1][j] == '1':
                union(i*M+j , (i-1)*M+j)

            if j > 0 and Map[i][j-1] == '1':
                union(i*M+j , i*M+j-1)

for i in range(N):
    for j in range(M):
        if Map[i][j] == '1':
            flag = True
            for island in islands:
                if find(i*M+j) == find(island[0]*M + island[1]):
                    flag = False
                    break
            if flag:
                islands.append([i,j])

# Row bridge
for i in range(N):
    l, r = -1, -1
    flag = False
    for j in range(M):
        if Map[i][j] == '0':
            if flag:
                r += 1
            else: # 새로운 다리 시작
                l = j
                r = j
                flag = True
                
        else: # 1
            flag = False
            if l > 0 and r-l >= 1: # Map[i][l-1] ~ Map[i][r+1]
                edges.append([find(i*M + l-1), find(i*M + r+1) , r-l+1])
            l, r = -1, -1


# Column bridge
for i in range(M):
    l, r = -1, -1
    flag = False
    for j in range(N):
        if Map[j][i] == '0':
            if flag:
                r += 1
            else: # 새로운 다리 시작
                l = j
                r = j
                flag = True
                
        else: # 1
            flag = False
            if l > 0 and r-l >= 1: # Map[l-1][i] ~ Map[r+1][i]
                edges.append([find((l-1)*M + i), find((r+1)*M + i) , r-l+1])
            l, r = -1, -1

cost = 0
edges.sort(key = lambda x : x[2])
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        cost += edge[2]

# 모든 섬이 연결되었는지 확인
flag = True
tmp = -1
for island in islands:
    if tmp == -1:
        tmp = find(island[0]*M + island[1])
    elif tmp != find(island[0]*M + island[1]):
        flag = False
        break
    
if flag:
    print(cost)
else:
    print(-1)