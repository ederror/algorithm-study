# Baekjoon - 16236
import sys
from collections import deque

input = sys.stdin.readline
drdc = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N = int(input())
board = [list(map(int, input().split())) for __ in range(N)]

r, c = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            r, c = i, j # 아기 상어 위치
            board[i][j] = 0

babyshark = 2
time = 0
num_eat = 0
while True:
    fish = []
    fish_t = 0
    queue = deque([(r,c,0)])
    visited = [(r,c)]
    while queue:
        cur_r, cur_c, t = queue.popleft()
        for dr, dc in drdc:
            next_r, next_c = cur_r + dr, cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < N and (next_r, next_c) not in visited:
                if board[next_r][next_c] <= babyshark:
                    if board[next_r][next_c] == 0 or board[next_r][next_c] == babyshark:
                        queue.append((next_r, next_c, t+1))
                        visited.append((next_r, next_c))
                    else: # 잡아먹을 물고기가 있을 때
                        if fish_t == 0 or fish_t == t+1:
                            fish.append((next_r, next_c))
                            fish_t = t+1
                        else:
                            queue = []
                            break
                else:
                    continue
    if fish:
        fish.sort(key=lambda x: (x[0], x[1]))
        r, c = fish[0][0], fish[0][1]
        board[r][c] = 0
        time += fish_t
        num_eat += 1
        if num_eat == babyshark:
            num_eat = 0
            babyshark += 1
    else:
        break
print(time)