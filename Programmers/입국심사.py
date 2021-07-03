# Programmers - 입국심사
def solution(n, times):
    minT = 0
    maxT = n * max(times)
    answer = maxT
    
    # Binary Search 
    while minT <= maxT:
        # 전체 소모 시간
        currentT = (minT + maxT) // 2
        
        # currentT 시간 안에 처리할 수 있는 사람 수
        num = 0 
        for time in times:
            num += currentT // time
        
        if num < n: # 시간 더 필요
            minT = currentT + 1
        else:
            # n명 이상의 사람을 처리할 수 있는 currentT 최소값 찾기
            if answer > currentT:
                answer = currentT
            maxT = currentT - 1
    
    return answer