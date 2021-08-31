# Baekjoon - 13460
import sys
input = sys.stdin.readline

def move(pos, dir):
    """ 현재 위치 pos, 방향 dir을 받아서  (ex. dir = [0:1] -> 위)
        dir 방향으로 최대한 (벽을 만날 때 까지) 움직인 후의 위치를 반환
    """
    nextPos = [pos[0], pos[1]]
    while 0<pos[0]<N and 0<pos[1]<M:
        nextPos[0] += dir[0]
        nextPos[1] += dir[1]
        if board[nextPos[0]][nextPos[1]] == '.':
            pos = [nextPos[0], nextPos[1]]
        elif board[nextPos[0]][nextPos[1]] == 'O':
            return [nextPos[0], nextPos[1]]
        else:
            break
    return pos

def whoIsFirst(R, B, dir):
    x, y = 0, 0
    if dir[0] == 0 and R[0] == B[0]:
        x, y = R[1], B[1]
        if dir[1] == -1:
            x *= -1
            y *= -1
    elif dir[1] == 0 and R[1] == B[1]:
        x, y = R[0], B[0]
        if dir[0] == -1:
            x *= -1
            y *= -1
    if x < y: # R - B - #
        return 0
    else: # B - R - #
        return 1

N, M = map(int, input().split())
R = [0,0]
B = [0,0]
O = [0,0]
board = []
for i in range(N):
    string = input()
    board.append(list(string))
    for j in range(M):
        if board[i][j] == 'R':
            R = [i,j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            B = [i,j]
            board[i][j] = '.'
        elif board[i][j] == 'O':
            O = [i,j]

answer = 0
queue = [[[R[0], R[1]], [B[0], B[1]], 0] ]
visited = [[R[0], R[1], B[0], B[1] ] ]
dirList = [[0,1], [0,-1], [1,0], [-1,0]]
while queue:
    R, B, cnt = queue.pop(0)
    if cnt > 10: # 계속 할 필요 없음
        break

    for dir in dirList:
        nextR = move(R, dir)
        nextB = move(B, dir)

        if nextR == nextB: # 두 구슬이 겹치는 경우 처리
            if nextR == O: # 둘이 동시에 구멍에 빠질 때
                continue
            flag = whoIsFirst(R, B, dir)
            if flag == 1: # B가 한칸 되돌아감
                nextB = [nextB[0] - dir[0] , nextB[1] - dir[1]]
            else:
                nextR = [nextR[0] - dir[0] , nextR[1] - dir[1]]

        if nextR == O: # 빨간 구슬이 구멍에 빠진 경우
            answer = cnt+1
            break

        if nextB == O or (nextR == R and nextB == B): # 파란 구슬이 빠지거나, 위치가 변경되지 않은 경우는 skip
            continue
        elif [nextR[0], nextR[1], nextB[0], nextB[1]] not in visited: # 그 외에는 방문했는지 확인하고 queue에 넣음
            visited.append([nextR[0], nextR[1], nextB[0], nextB[1]])
            queue.append([[nextR[0], nextR[1]], [nextB[0], nextB[1]], cnt+1])

    if answer != 0:
        break

if answer == 0 or answer > 10:
    print(-1)
else:
    print(answer)