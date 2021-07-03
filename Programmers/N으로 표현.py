# Programmers - N으로 표현
def solution(N, number):
    # 예외처리
    if N == number:
        return 1
    
    answer = 0

    # N을 i+1번 사용해서 만들 수 있는 수 => set dp[i] 
    dp = [set() for _ in range(8)]

    tmp = N
    dp[0].add(tmp)
    for i in range(1,8):
        tmp = tmp*10 + N
        dp[i].add(tmp) # N, NN, NNN, NNNN ...
        
        for j in range(i):
            # dp[i-j-1] : N을 i-j번 사용해서 만들 수 있는 수
            # dp[j] : N을 j+1번 사용해서 만들 수 있는 수
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0 and op1 % op2 == 0:
                        dp[i].add(op1 // op2)
                        
        if number in dp[i]:
            return i+1

    # 발견 못한 경우
    return -1