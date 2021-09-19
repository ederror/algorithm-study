# Baekjoon - 14499
import sys
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0 for __ in range(6)]

N, M, x, y, K = map(int ,input().split())
board = []
for __ in range(N):
    board.append(list(map(int, input().split())))
instructions = map(int, input().split())

for inst in instructions:
    next_x, next_y = x + dx[inst], y + dy[inst]
    if not(0<= next_x < N and 0<= next_y < M): 
        continue
    else:
        x, y = next_x, next_y

    # 주사위 굴리기
    if inst == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif inst == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif inst == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif inst == 4:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[0]) # 주사위 밑면 수 출력