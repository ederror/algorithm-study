# Baekjoon - 15683
import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def backtrack(board, cidx):
    global answer
    if cidx == len(cctv):
        cnt = sum([row.count(0) for row in board])
        if cnt < answer:
            answer = cnt
        return

    ctype, r, c = cctv[cidx]
    for rotate in range(rotatenum[ctype]):
        nboard = deepcopy(board)
        for didx in cctvtype[ctype]:
            dr, dc = d[(didx+rotate) % 4]
            i, j = r, c
            while 0<= i < N and 0<= j < M:
                if nboard[i][j] == 6:
                    break
                elif nboard[i][j] == 0:
                    nboard[i][j] = -1
                i += dr
                j += dc
        backtrack(nboard, cidx+1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for __ in range(N)]

cctv = []
d = [[-1,0], [0, 1], [1,0], [0,-1]]
cctvtype = [0, [0], [0, 2], [0, 1], [0,1,2], [0,1,2,3]]
rotatenum = [0, 4, 2, 4, 4, 1]

for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 6:
            cctv.append([board[i][j],i,j])

answer = 64
backtrack(board, 0)
print(answer)