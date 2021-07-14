# Programmers - 거스름돈
def solution(n, money):
    # dp[i][j] : money[0] ~ money[i]를 사용해 j원을 만드는 경우의 수
    dp = [[0 for _ in range(n+1)] for _ in range(len(money))]
    
    # 1st row
    for j in range(n+1):
        if j % money[0] == 0:
            dp[0][j] = 1
    
    # 2nd row ~
    for i in range(1, len(money)):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j]
            
            if j-money[i] >= 0:
                dp[i][j] = (dp[i][j] + dp[i][j-money[i]]) % 1000000007
                
    return dp[len(money)-1][n] % 1000000007