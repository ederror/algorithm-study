# Baekjoon - 11659
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))
for i in range(1, N):
    seq[i] += seq[i-1]

for __ in range(M):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    answer = seq[j]
    if i>0:
        answer -= seq[i-1]
    print(answer)