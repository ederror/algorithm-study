# Baekjoon - 10217
import sys
input =  sys.stdin.readline
INF = sys.maxsize

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    graph = [[INF, INF]*N for _ in range(N)] # [cost, distance]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u-1][v-1][0] = c
        graph[u-1][v-1][1] = d
    