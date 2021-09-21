# Baekjoon - 14503
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(r,c,d):
    if [r,c] not in clean:
        clean.append([r,c])

    for d in range(d-1, d-5, -1):
        d %= 4
        dr, dc = dir[d]
        next_r, next_c = r+dr, c+dc
        if board[next_r][next_c] == 0 and [next_r, next_c] not in clean:
            DFS(next_r, next_c, d)
            break
    else:
        dr, dc = dir[(d+2)%4]
        next_r, next_c = r+dr, c+dc
        if board[next_r][next_c] == 0:
            DFS(next_r, next_c, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
dir = [[-1, 0], [0,1], [1,0], [0,-1]]

board = []
for __ in range(N):
    board.append(list(map(int, input().split())))

clean = []
DFS(r,c,d)
print(len(clean))