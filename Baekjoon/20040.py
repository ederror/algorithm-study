# Baekjoon - 20040
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
        
n, m = map(int, input().split())
parent =  [i for i in range(n)]
rank = [1] * n
flag = 0
for i in range(m):
    v, w = map(int, input().split())

    if find(v) == find(w):
        if flag == 0:
            flag = i+1
    else:
        union(v, w)

print(flag)