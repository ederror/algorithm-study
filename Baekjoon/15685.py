# Baekjoon - 15685
import sys
input = sys.stdin.readline

def next_gen(generation, x, y): # x, y 기준점
    global direction, d, dc
    nx, ny = 0, 0
    newdc = [(cx, cy) for cx, cy in dc] # deep copy
    
    if generation == 0:
        nx, ny = x + direction[d][0], y + direction[d][1]
        dc.append((nx, ny)) # (x,y) -> (nx, ny)
    else: 
        for cx, cy in dc:
            if cx == x and cy == y:
                continue
            newdc.append((x + y - cy, y + cx - x))
        nx, ny = x + y - sy, y + sx - x
        dc = newdc
    return nx, ny
    
direction = [[1,0], [0, -1], [-1, 0], [0, 1]]
N = int(input())
coords = [] # 전체 좌표 모음
for __ in range(N):
    x, y, d, g = map(int, input().split())
    sx, sy = x, y # 시작점 기록
    dc = [(x,y)]
    for gen in range(g+1):
        x, y = next_gen(gen, x, y)
    coords.extend(dc)

answer = 0
coords = set(coords)
for x, y in coords:
    if ( (x,y) in coords 
            and (x+1, y) in coords
            and (x, y+1) in coords
            and (x+1, y+1) in coords ):
        answer += 1
print(answer)