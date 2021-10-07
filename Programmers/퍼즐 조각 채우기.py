# Programmers - 퍼즐 조각 채우기
from copy import deepcopy

def normalize(block):
    min_r, min_c = 9999, 9999
    for r, c in block:
        if r < min_r:
            min_r = r
        if c < min_c:
            min_c = c
    
    for i in range(len(block)):
        block[i][0] -= min_r
        block[i][1] -= min_c
        

def rotate(block):
    for i in range(len(block)):
        r, c = block[i]
        block[i] = [c, -r]
    normalize(block)


def find_blocks(board, x):
    drdc = [(0,1), (0,-1), (1,0), (-1,0)]
    N = len(board)
    blocks = []
    visited = [[0]*N for __ in range(N)]
    
    for i in range(N):
        for j in range(N):
            # BFS
            if not visited[i][j] and board[i][j] == x:
                new_block = [[i,j]]
                queue = [[i,j]]
                visited[i][j] = 1
                while queue:
                    r, c = queue.pop(0)
                    for dr, dc in drdc:
                        if not (0 <= r+dr < N and 0 <= c+dc < N):
                            continue
                        if board[r+dr][c+dc] == x and visited[r+dr][c+dc] == 0:
                            queue.append([r+dr, c+dc])
                            new_block.append([r+dr, c+dc])
                            visited[r+dr][c+dc] = 1
                normalize(new_block)
                blocks.append(new_block)
    return blocks


def compare_block(block1, block2):
    block2_cp = deepcopy(block2)
    for r,c in block1:
        try:
            block2_cp.remove([r,c])
        except:
            return False
    if not block2_cp:
        return True
    return False


def solution(game_board, table):
    answer = 0
    
    g_blocks = find_blocks(game_board, 0)
    t_blocks = find_blocks(table, 1)
    
    block_used = [0] * len(t_blocks)
    for block in g_blocks:
        for i, t_block in enumerate(t_blocks):
            if block_used[i]:
                continue
            
            didFit = False
            for __ in range(4): # rotate
                rotate(t_block)
                if compare_block(block, t_block):
                    block_used[i] = 1
                    answer += len(block)
                    didFit = True
                    break
            if didFit:
                break
    return answer