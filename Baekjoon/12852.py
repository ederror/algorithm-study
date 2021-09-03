# Baekjoon - 12852
import sys
input = sys.stdin.readline

INF = 10**6
N = int(input())

dp = [INF] * (N+1)
parent = [0] * (N+1)

dp[1] = 0
for i in range(2, N+1):
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        parent[i] = i//2
    
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        parent[i] = i//3

    if dp[i] > dp[i-1] + 1:
        dp[i] = dp[i-1] + 1
        parent[i] = i-1

print(dp[N])
while N >= 1:
    print(N, end=" ")
    N = parent[N]