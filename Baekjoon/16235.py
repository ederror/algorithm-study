# Baekjoon - 16235
import sys
from collections import deque

input = sys.stdin.readline

drdc = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for __ in range(N)]
tree = [[deque([]) for __ in range(N)] for __ in range(N)]
ground = [[5]*N for __ in range(N)]
answer = 0
for __ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
    answer += 1

for k in range(K):
    if answer == 0:
        break

    # 봄
    for i in range(N):
        for j in range(N):
            dead_tree = 0
            for tidx, t in enumerate(tree[i][j]):
                if ground[i][j] >= t:
                    ground[i][j] -= t
                    tree[i][j][tidx] += 1
                else: # 이후로는 모두 양분이 부족해서 죽음
                    for _ in range(tidx, len(tree[i][j])):
                        dead_tree += tree[i][j].pop() // 2
                        answer -= 1
                    ground[i][j] += dead_tree # 여름
                    break

    # 가을
    for i in range(N):
        for j in range(N):
            for t in tree[i][j]:
                if t % 5 != 0:
                    continue
                
                for dr, dc in drdc:
                    if not (0<= i+dr <N and 0<= j+dc < N):
                        continue
                    tree[i+dr][j+dc].appendleft(1)
                    answer += 1

    # 겨울
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]
print(answer)