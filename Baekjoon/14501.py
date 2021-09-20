# Baekjoon - 14501
import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
answer = 0
for day in range(N):
    t, p = map(int, input().split())
    if day > 0 and dp[day] < dp[day-1]:
        dp[day] = dp[day-1]

    if day+t <= N and dp[day+t] < dp[day] + p:
        dp[day+t] = dp[day] + p
print(max(dp[N-1], dp[N]))