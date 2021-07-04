# Programmers - 순위
def solution(n, results):
    answer = 0
    l = [[0 for _ in range(n) ] for _ in range(n)]
    
    for result in results:
        l[result[0]-1][result[1]-1] = 1
        l[result[1]-1][result[0]-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # i-> k -> j
                if l[i][k] == 1 and l[k][j] == 1:
                    l[i][j] = 1
                elif l[i][k] == -1 and l[k][j] == -1:
                    l[i][j] = -1

    for i in range(n):
        if l[i].count(0) == 1: # l[i][i]
            answer += 1
    return answer