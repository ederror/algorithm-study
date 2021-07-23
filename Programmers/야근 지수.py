# Programmers - 야근 지수
import heapq

def solution(n, works):
    answer = 0
    works = list(map(lambda x: -x, works)) # minheap을 maxheap처럼 사용하기 위해 음수화
    works.sort()
    
    while n > 0:
        work = heapq.heappop(works) # 가장 많이 남은 작업량
        if work == 0:
            break
        
        work += 1
        n -= 1
        heapq.heappush(works, work)
        
    for work in works:
        answer += work*work
    return answer