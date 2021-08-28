# Programmers - 외벽 점검
from itertools import permutations
def solution(n, weak, dist):
    
    numOfWeak = len(weak)
    answer= len(dist) + 1
    dists = permutations(dist, len(dist))
    weak = weak + [w+n for w in weak]

    for dist in dists:
        for i in range(numOfWeak): # weak[i] : 시작점
            visit = []
            for cnt, d in enumerate(dist):
                s = weak[i]
                while i < len(weak) and weak[i] <= s+d:
                    visit.append(weak[i])
                    i += 1

                if len(visit) >= numOfWeak: # 모두 방문 완료
                    answer = min(answer, cnt+1)

                if i >= len(weak):
                    break

    if answer > len(dist):
        return -1
    else:
        return answer