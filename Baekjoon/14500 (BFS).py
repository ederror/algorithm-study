# Baekjoon - 14500 (BFS)
import sys
import heapq
input = sys.stdin.readline

def BFS(r, c):
    queue = [(-board[r][c], (r,c))] # Max Heap
    visited = []
    while True:
        s, cur = heapq.heappop(queue)
        cur_r, cur_c = cur
        visited.append(cur)
        
        if len(visited) == 4:
            break

        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            next_r, next_c = cur_r+dr, cur_c+dc
            if 0<=next_r<N and 0<=next_c<M and (next_r,next_c) not in visited:
                heapq.heappush(queue, (-board[next_r][next_c], (next_r, next_c)))
    return sum([board[r][c] for r, c in visited])

board = []
N, M = map(int, input().split())
for __ in range(N):
    board.append(list(map(int, input().split())))

answer = 0
for r in range(N):
    for c in range(M):
        tmpsum = BFS(r,c)
        if answer < tmpsum:
            answer = tmpsum
print(answer)