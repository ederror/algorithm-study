# Baekjoon - 2667
import sys
input = sys.stdin.readline

N = int(input())
Map = [[] for _ in range(N)]
queue = []
visited = []
dx = [0, 0, +1, -1]
dy = [+1, -1, 0, 0]
answer = []
for i in range(N):
    inputLine = input()
    for c in inputLine[:-1]:
        Map[i].append(int(c))

for i in range(N):
    for j in range(N):
        if Map[i][j] == 1 and (i,j) not in visited:
            # BFS
            cnt = 1
            queue.append((i,j))
            visited.append((i,j))
            while queue:
                x, y = queue.pop(0)
                for idx in range(4):
                    newX, newY = x+dx[idx], y+dy[idx]
                    if newX >= 0 and newX < N and newY >= 0 and newY < N:
                        if (newX, newY) not in visited and Map[newX][newY] == 1:
                            queue.append((newX, newY))
                            visited.append((newX, newY))
                            cnt += 1
            answer.append(cnt)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)