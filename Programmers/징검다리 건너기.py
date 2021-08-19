# Programmers - 징검다리 건너기
def solution(stones, k):
    answer = 0
    s, e = 0, max(stones)
    
    while s <= e:
        m = (s+e) // 2
        
        cnt = 0 # 연속되는 0이하 수의 개수
        for stone in stones:
            if stone-m <= 0:
                cnt += 1
            else:
                cnt= 0
                
            if cnt >= k:
                e = m-1
                break
        
        if cnt < k: # 더 많은 친구가 건널 수 있음
            s = m+1
        answer = s
    
    return answer