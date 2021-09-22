# Baekjoon - 14890
import sys
input = sys.stdin.readline

def checkRoad(seq):
    installed = [0]*N
    i, cur=1, seq[0]
    while i < N:
        if cur == seq[i]:
            i += 1
        elif cur == seq[i]-1: # /
            j, cnt = i-1, 0
            while j >= 0 and cnt < L:
                if not installed[j] and seq[j] == cur:
                    installed[j] = 1
                    cnt += 1
                    j -= 1
                else:
                    break
            if cnt != L:
                return False
            cur = seq[i]
            i += 1
        elif cur == seq[i]+1: # \
            j, cnt = i, 0
            while j <N and cnt < L:
                if not installed[j] and seq[j] == seq[i]:
                    installed[j] = 1
                    cnt += 1
                    j += 1
                else:
                    break
            if cnt != L:
                return False
            cur = seq[i]
            i += 1
        else:
            return False
    return True

answer = 0
N, L = map(int, input().split())
board = []
for __ in range(N):
    board.append(list(map(int, input().split())))

for row in board:
    if checkRoad(row):
        answer += 1

for col in range(N):
    if checkRoad([b[col] for b in board]):
        answer += 1
print(answer)