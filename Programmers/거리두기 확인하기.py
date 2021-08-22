# Programmers - 거리두기 확인하기
def solution(places):
    
    def check(i, j, place):
        # 1. 상하좌우에 P가 있나 확인
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            if 0<=i+dx<5 and 0<=j+dy<5:
                if place[i+dx][j+dy] == 'P':
                    return 0

        # 2. 맨해튼 거리가 2인 곳에 P가 있는지
        for dx, dy in z:
            if not(0<=i+dx<5 and 0<=j+dy<5):
                continue

            if place[i+dx][j+dy] == 'P':
                cnt = 0
                for cx, cy in z[(dx,dy)]:
                    if place[i+cx][j+cy] == 'X':
                        cnt += 1                    
                if cnt != len(z[(dx,dy)]):
                    return 0
        return 1 # 거리두기 잘된 경우
            
    answer = []
    z = {(0, -2): [[0, -1]], (1, -1): [[0,-1],[1,0]], (2, 0): [[1,0]], (1, 1): [[1,0], [0,1]], (0, 2): [[0,1]], (-1, 1): [[-1,0], [0,1]], (-2, 0): [[-1,0]], (-1, -1): [[0, -1], [-1,0]]}
    
    for place in places:
        isGood = True
        for i in range(5):
            for j in range(5):
                if place[i][j] =='P' and check(i,j, place) == 0:
                    isGood = False
                    break
        if isGood:
            answer.append(1)
        else:
            answer.append(0)
                
    return answer