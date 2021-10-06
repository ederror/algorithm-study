# Baekjoon - 17144
import sys
from collections import defaultdict

input = sys.stdin.readline

R, C, T = map(int, input().split())
drdc = [(0,1), (0,-1), (1,0), (-1,0)]
room = []
cleaner = -1

for r in range(R):
    room.append(list(map(int, input().split())))
    if cleaner == -1 and room[r][0] == -1:
        cleaner = r

for __ in range(T):
    updatedust = defaultdict(int)
    for r in range(R):
        for c in range(C):
            if room[r][c] == 0 or room[r][c] == -1:
                continue
            for dr, dc in drdc:
                if not (0 <= r+dr < R and 0 <= c+dc < C) or room[r+dr][c+dc] == -1:
                    continue
                updatedust[(r+dr, c+dc)] += room[r][c] // 5
                updatedust[(r,c)] -= room[r][c] // 5

    for key in updatedust:
        r, c = key
        room[r][c] += updatedust[key]


    # 반시계 방향 바람
    for i in range(cleaner-2, -1, -1):
        room[i+1][0] = room[i][0]
    for j in range(1, C):
        room[0][j-1] = room[0][j]
    for i in range(1, cleaner+1):
        room[i-1][C-1] = room[i][C-1]
    for j in range(C-1, 1, -1):
        room[cleaner][j] = room[cleaner][j-1]
    room[cleaner][1] = 0

    # 시계 방향 바람
    for i in range(cleaner+2,R-1):
        room[i][0] = room[i+1][0]
    for j in range(0, C-1):
        room[R-1][j] = room[R-1][j+1]
    for i in range(R-1, cleaner+1, -1):
        room[i][C-1] = room[i-1][C-1]
    for j in range(C-1, 1, -1):
        room[cleaner+1][j] = room[cleaner+1][j-1]
    room[cleaner+1][1] = 0

answer = 2
for i in range(R):
    for j in range(C):
        answer += room[i][j]
print(answer)