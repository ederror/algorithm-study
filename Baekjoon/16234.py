# Baekjoon - 16234
import sys
from collections import deque
input = sys.stdin.readline

drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for __ in range(N)]

done = False
day = -1
while not done:
    day += 1
    done = True
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0:
                done = False
                continue
            union = [(i,j)]
            queue = deque([(i,j)])
            visited[i][j] = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in drdc:
                    if not (0 <= r+dr < N and 0 <= c+dc < N):
                        continue

                    if visited[r+dr][c+dc] == 0 and L <= abs(A[r][c] - A[r+dr][c+dc]) <= R:
                        visited[r+dr][c+dc] = 1
                        queue.append((r+dr, c+dc))
                        union.append((r+dr, c+dc))
            
            avg = sum([A[ii][jj] for ii, jj in union]) // len(union)
            if len(union) != 1:
                for ii, jj in union:
                    A[ii][jj] = avg
print(day)