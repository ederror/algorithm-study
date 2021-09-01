# Programmers - 삼각 달팽이
def solution(n):
    triangle = [[0]*i for i in range(1, n+1)]
    x, y = 0, 0
    triangle[x][y] = 1
    cnt = 1
    while cnt < n*(n+1)//2 :
        while x+1 < n and triangle[x+1][y] == 0:
            x += 1
            cnt += 1
            triangle[x][y] = cnt
        
        while y+1 < len(triangle[x]) and triangle[x][y+1] == 0:
            y += 1
            cnt += 1
            triangle[x][y] = cnt
        
        while triangle[x-1][y-1] == 0:
            x -= 1
            y -= 1
            cnt += 1
            triangle[x][y] = cnt

    answer = []
    for t in triangle:
        answer.extend(t)
    return answer