# Programmers - 징검다리
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    s, e = 0, distance
    while s <= e:
        m = (s+e) // 2 
        deleted = 0
        pivot = 0
        for rock in rocks:
            if rock-pivot >= m:
                pivot = rock
            else:
                deleted += 1
                
        if pivot != 0 and distance - pivot < m:
            deleted += 1

        if deleted <= n:
            answer = max(m, answer)
            s = m+1
        else:
            e = m-1
            
    return answer