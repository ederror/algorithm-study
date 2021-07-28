# Programmers - 멀리 뛰기
def solution(n):
    dp = [1, 2]
    if n > 2:
        dp += [0] * (n-2)
    
    for i in range(2, n):
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567
    
    return dp[n-1] % 1234567