# Baekjoon - 13458
import sys
import math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for a in A:
    a -= B
    answer += 1 # 총감독
    if a > 0:
        answer += math.ceil(a/C)
print(answer)