# Programmers - 경주로 건설
def solution(board):
    N = len(board)
    cost = [[float("INF")]*N for _ in range(N)]
    isHorizontal = [[0]*N for _ in range(N)] # 수평으로 연결된 도로인가
    move = [[0,1], [0,-1], [1,0], [-1,0]]
    
    Q = [[0,0]]
    isHorizontal[0][0] = -1
    cost[0][0] = 0
    while Q:
        x, y = Q.pop(0)
        for dx, dy in move:
            if x+dx>=0 and x+dx<N and y+dy>=0 and y+dy<N:
                if board[x+dx][y+dy] == 1: # 이동하려는 곳이 벽인 경우
                    continue
                nextCost = cost[x][y] + 100 # 직선도로 비용 추가
                
                # 코너비용 추가
                if isHorizontal[x][y] == 0 and dx == 0:
                    nextCost += 500 
                elif isHorizontal[x][y] == 1 and dy == 0:
                    nextCost += 500
                    
                # 비용이 더 적으면 update 후 다시 Q에 넣어서 나중에 탐색
                if cost[x+dx][y+dy] > nextCost:
                    cost[x+dx][y+dy] = nextCost
                    if dx == 0:
                        isHorizontal[x+dx][y+dy] = 1
                    else:
                        isHorizontal[x+dx][y+dy] = 0
                    Q.append([x+dx, y+dy])
                
                # 수평, 수직 모든 방향에서 최소 비용으로 건설 가능 -> -1
                elif cost[x+dx][y+dy] == nextCost: 
                    if isHorizontal[x+dx][y+dy] == 0 and dx == 0:
                        isHorizontal[x+dx][y+dy] = -1
                    if isHorizontal[x+dx][y+dy] == 1 and dy == 0:
                        isHorizontal[x+dx][y+dy] = -1
                    
    return cost[N-1][N-1]