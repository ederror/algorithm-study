# Programmers - 등굣길
def solution(m, n, puddles):
    dist = [[0 for _ in range(m)] for _ in range(n)]
    
    for puddle in puddles:
        dist[puddle[1]-1][puddle[0]-1] = -1
    
    dist[0][0] = 1
    for i in range(n):
        for j in range(m):
            if dist[i][j] == -1: # 물 웅덩이
                dist[i][j] = 0
                continue
                
            if i > 0:
                dist[i][j] = (dist[i][j] + dist[i-1][j]) % 1000000007
            if j > 0:
                dist[i][j] = (dist[i][j] + dist[i][j-1]) % 1000000007
    
    return dist[n-1][m-1] % 1000000007