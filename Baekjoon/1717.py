# Baekjoon - 1717
import sys
sys.setrecursionlimit(10 ** 6)
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
    
    if rank[x] > rank[y]: # x가 더 깊은 트리 => y를 x쪽에 붙임
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
        
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [1] * (n+1)

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: # a가 포함된 집합과 b가 포함된 집합 합침.
        union(a, b)
    else: # a가 포함된 집합과 b가 포함된 집합이 같은지 확인.
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")