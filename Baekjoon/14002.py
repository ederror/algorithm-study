# Baekjoon - 14002
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
maxVal, maxIdx = 1, 0
dp = [1]*N
parent = [-1]*N
for i in range(1, N):
    for j, a in enumerate(A[:i]):
        if a < A[i]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                parent[i] = j
    if maxVal < dp[i]:
        maxVal, maxIdx = dp[i], i

print(maxVal)

stack = []
while maxIdx > -1:
    stack.append(A[maxIdx])
    maxIdx = parent[maxIdx]

while stack:
    print(stack.pop(), end=" ")