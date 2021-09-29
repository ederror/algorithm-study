# Baekjoon - 15686
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
house = []
chicken = []
dists = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append((i,j))
        elif row[j] == 2:
            chicken.append((i,j))

answer = float('inf')
for chicken_comb in combinations(chicken, M):
    dists = []
    for h in house:
        dist = 9999
        for c in chicken_comb:
            dist_cur = abs(h[0] - c[0]) + abs(h[1] - c[1])
            if dist > dist_cur:
                dist = dist_cur
        dists.append(dist)
    sum_ = sum(dists)
    if answer > sum_:
        answer = sum_
print(answer)