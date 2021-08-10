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
for _ in range(N):
    x, y, z = map(int, input().split())
    planet.append([x, y, z])
print(planet)
planet.sort(key = lambda x: (x[0], x[1], x[2]))
print(planet)

for i in range(N):
    for j in range(i+1, N):
        cost = min(abs(planet[i][0] - planet[j][0]) , abs(planet[i][1] - planet[j][1]), abs(planet[i][2] - planet[j][2]))
        edge.append([i, j, cost])
        
edge.sort(key = lambda x : x[2])

cnt = 0
answer = 0
while cnt < N-1 :
    e = edge.pop(0)
    if find(e[0]) != find(e[1]):
        union(e[0], e[1])
        answer += e[2]
        cnt += 1
print(answer)
