# Baekjoon - 14500
import sys
input = sys.stdin.readline

def rotate(block): 
    rblock = []
    rMin, cMin = 4, 4
    for x, y in block:
        rblock.append([3-y, x])
        if rMin > 3-y:
            rMin = 3-y
        if cMin > x:
            cMin = x
    for i, b in enumerate(rblock):
        rblock[i] = [b[0]-rMin, b[1]-cMin]
    return rblock

def flip(block):
    fblock = []
    cMin = 4
    for x, y in block:
        fblock.append([x, 3-y])
        if cMin > 3-y:
            cMin = 3-y
    for i, b in enumerate(fblock):
        fblock[i] = [b[0], b[1]-cMin]
    return fblock

def blockSum(x,y,block):
    sum = 0
    for r, c in block:
        if 0<=x+r<N and 0<=y+c<M:
            sum += board[x+r][y+c]
        else:
            return 0
    return sum

N, M = map(int, input().split())
answer = 0
board = []
for __ in range(N):
    board.append(list(map(int, input().split())))

blocks = [
    [[0,0], [0,1], [0,2], [0,3]],
    [[0,0], [0,1], [1,0], [1,1]],
    [[0,0], [1,0], [2,0], [2,1]],
    [[0,0], [1,0], [1,1], [2,1]],
    [[0,0], [0,1], [0,2], [1,1]]]

for block_idx in range(5):
    curBlock = blocks[block_idx]
    for _ in range(2): # flip
        for __ in range(3): # rotate
            curBlock = rotate(curBlock)
            blocks.append(curBlock)
        curBlock = flip(blocks[block_idx])
        blocks.append(curBlock)

for x in range(N):
    for y in range(M):
        for block in blocks:
            sum = blockSum(x, y, block)
            if answer < sum:
                answer = sum
print(answer)