# Baekjoon - 2887
import sys
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
    else:
        parent[x] = y

N = int(input())
parent = [i for i in range(N)]
planet = []
edge = []
for i in range(N):
    x, y, z = map(int, input().split())
    planet.append([i, x, y, z])

for i in range(1, 4):
    planet.sort(key = lambda x : x[i])
    for j in range(N-1):
        p1, p2 = planet[j], planet[j+1]
        edge.append([p1[0], p2[0], abs(p1[i] - p2[i])])
    
edge.sort(key = lambda x : x[2])

answer = 0
for e in edge:
    if find(e[0]) != find(e[1]):
        union(e[0], e[1])
        answer += e[2]
print(answer)