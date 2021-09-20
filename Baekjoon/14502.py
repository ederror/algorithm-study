# Baekjoon - 14502
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def BFS(bd, r, c):
    cnt = 1
    queue = deque([(r,c)])
    while queue:
        cur_r, cur_c = queue.popleft()

        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            next_r, next_c = cur_r+dr, cur_c+dc
            if 0<=next_r<N and 0<=next_c<M and bd[next_r][next_c] == 0:
                queue.append((next_r, next_c))
                bd[next_r][next_c] = 2
                cnt += 1
    return cnt


N, M = map(int, input().split())
board = []
virus = []
cand = []
numOfWalls = 3
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i,j))
        elif board[i][j] == 1:
            numOfWalls += 1
        else:
            cand.append((i,j))

comb = combinations(cand, 3)
answer = 0
for w1, w2, w3 in comb:
    bd = deepcopy(board)
    bd[w1[0]][w1[1]] = 1
    bd[w2[0]][w2[1]] = 1
    bd[w3[0]][w3[1]] = 1
    cnt = 0
    for r, c in virus:
        cnt += BFS(bd,r,c)

    if answer < N*M-cnt-numOfWalls:
        answer = N*M-cnt-numOfWalls
print(answer)