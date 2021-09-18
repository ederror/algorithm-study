# Baekjoon - 12100
import sys
input = sys.stdin.readline

def push(seq):
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            seq[i] *= 2
            seq[i+1] = 0

    while True:
        try:
            seq.remove(0)
        except:
            break
    return seq

def up(board):
    new_board = [[e for e in row] for row in board]
    for c in range(N):
        seq = []
        for r in range(N):
            if new_board[r][c] != 0:
                seq.append(new_board[r][c])
        seq = push(seq)
        seq = seq + [0] * (N-len(seq))
        for r in range(N):
            new_board[r][c] = seq[r]
    return new_board

def down(board):
    new_board = [[e for e in row] for row in board]
    for c in range(N):
        seq = []
        for r in range(N-1, -1, -1):
            if new_board[r][c] != 0:
                seq.append(new_board[r][c])
        seq = push(seq)
        seq = seq + [0] * (N-len(seq))
        for r in range(N-1, -1, -1):
            new_board[r][c] = seq[N-1-r]
    return new_board

def left(board):
    new_board = [[e for e in row] for row in board]
    for r in range(N):
        seq = []
        for c in range(N):
            if board[r][c] != 0:
                seq.append(board[r][c])
        seq = push(seq)
        seq = seq + [0] * (N-len(seq))
        for c in range(N):
            new_board[r][c] = seq[c]
    return new_board

def right(board):
    new_board = [[e for e in row] for row in board]
    for r in range(N):
        seq = []
        for c in range(N-1, -1, -1):
            if new_board[r][c] != 0:
                seq.append(new_board[r][c])
        seq = push(seq)
        seq = seq + [0] * (N-len(seq))
        for c in range(N-1, -1, -1):
            new_board[r][c] = seq[N-1-c]
    return new_board

def maxOnBoard(board):
    maximum = 0
    for row in board:
        maxrow = max(row)
        if maximum < maxrow:
            maximum = maxrow
    return maximum

N = int(input())
board = []
for __ in range(N):
    board.append(list(map(int, input().split())))

queue = [(board, 0)]
answer = 0
while queue:
    cur_board, cnt = queue.pop(0)
    maxval = maxOnBoard(cur_board)
    if answer < maxval:
        answer = maxval
    
    if cnt < 5:
        queue.append((up(cur_board), cnt+1))
        queue.append((down(cur_board), cnt+1))
        queue.append((left(cur_board), cnt+1))
        queue.append((right(cur_board), cnt+1))

print(answer)