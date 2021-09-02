# Programmers - 도둑질
def solution(money):
    answer = 0
    dp = [0] * len(money)
    
    # 마지막 제외
    dp[0], dp[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    answer = dp[len(money)-2]
    
    # 첫번째 제외
    dp[0], dp[1] = 0, money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    answer = max(answer, dp[len(money)-1])
    
    return answer