# Baekjoon - 1976
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
    
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]

n = int(input())
m = int(input())

parent = [i for i in range(n)]
rank = [1] * n

for v in range(n):
    tmp = list(map(int, input().split()))
    for w in range(n):
        if tmp[w] == 1 and find(v) != find(w):
            union(v, w)
        
plan = list(map(int, input().split()))
flag = 0
for v in plan:
    if find(plan[0]-1) != find(v-1):
        flag = 1
        break

if flag == 0:
    print("YES")
else:
    print("NO")