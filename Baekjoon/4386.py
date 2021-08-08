# Baekjoon - 4386
import sys
import math
input = sys.stdin.readline

n = int(input())

stars = []
graph = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    x, y = map(float, input().split())
    for star in enumerate(stars):
        graph[i][star[0]] = math.sqrt((x-star[1][0]) ** 2 + (y-star[1][1]) ** 2 )
        graph[star[0]][i] = graph[i][star[0]]
    stars.append([x,y])

mst = [0]
distance = graph[0]
answer = 0
# Prim
for _ in range(n-1):
    minIdx, minDist = -1, 1000000
    for idx, dist in enumerate(distance):
        if idx not in mst and dist <= minDist:
            minDist = dist
            minIdx = idx
    answer += minDist
    mst.append(minIdx)
    
    for i in range(n):
        if i != minIdx and distance[i] > graph[minIdx][i]:
            distance[i] = graph[minIdx][i]
print(answer)