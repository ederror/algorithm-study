# Baekjoon - 3190
import sys
from collections import deque
input = sys.stdin.readline

d = [[0,1], [1, 0], [0, -1], [-1, 0]]
dir_info = deque([])

N = int(input())
board = [[0]*N for __ in range(N)]

K = int(input())
for __ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
for __ in range(L):
    x, c = input().split()
    dir_info.append([int(x),c])

time = 0
curD = 0
cur = [0,0]
board[0][0] = 2
snake = deque([[0,0]])

while True:
    time += 1

    # 벽을 만났을 때 or 자기 몸을 만났을 때
    next = [cur[0]+d[curD][0], cur[1]+d[curD][1]]
    if not(0<=next[0]<N and 0<=next[1]<N) or board[next[0]][next[1]] == 2:
        break

    if board[next[0]][next[1]] == 0: # 빈칸일 때 -> 꼬리 지움
        r, c = snake.popleft()
        board[r][c] = 0

    board[next[0]][next[1]] = 2
    snake.append(next)
    cur = next

    if dir_info and dir_info[0][0] == time:
        _, c = dir_info.popleft()
        if c == 'D':
            curD = (curD+1) % 4
        else:
            curD = (curD+3) % 4
print(time)