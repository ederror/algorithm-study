# Baekjoon - 10217
import sys
input =  sys.stdin.readline
INF = sys.maxsize

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    #edges = [[] for _ in range(N)]
    edges = []
    dp = [[INF]*N for _ in range(M)]
    dp[0][0] = 0
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        #edges[v-1].append([u-1, c, d]) # v로 도착하는 엣지들 저장
        edges.append[[u-1, v-1, c, d]]
        
    for m in range(M):
        for u in range(N):
            if m > 0:
                dp[m][u] = dp[m-1][u]
                
            for edge in edges[u]:
                v, c, d = edge # v->u 비용c 시간d
                if m-c >= 0:
                    dp[m][u] = min(dp[m][u], dp[m-c][v] + d)
    
    for edge in edges:
        u, v, c, d = edge # u->v
        if d >= M:
            continue
        
        minValue = INF
        for i in range(d):
            minValue = min(minValue, dp[i][v])
        
        dp[d][v] = dp[] + d
        
        
    if dp[M-1][N-1] >= INF:
        print("Poor KCM")
    else:
        print(dp[M-1][N-1])