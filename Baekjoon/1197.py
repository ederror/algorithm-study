# Baekjoon - 1197
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    parent[y] = x
    
V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edge = []
mstWeight, cnt = 0, 0
for _ in range(E):
    v, w, weight =  map(int, input().split())
    edge.append([v, w, weight])
    
edge.sort(key = lambda x : x[2])
while cnt < V-1:
    v, w, weight = edge.pop(0)
    
    if find(v) != find(w):
        union(v, w)
        mstWeight += weight
        cnt += 1
        
print(mstWeight)