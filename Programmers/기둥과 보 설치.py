# Programmers - 기둥과 보 설치
def solution(n, build_frame):
    def check0(x, y): # 기둥이 적절하게 있는지 확인
        return (y==0 or [x,y-1] in installed[0] 
                or [x-1,y] in installed[1] or [x,y] in installed[1])
    def check1(x, y) : # 보가 적절하게 있는지 확인
        return ([x,y-1] in installed[0] or [x+1,y-1] in installed[0]
                or ([x-1,y] in installed[1] and [x+1,y] in installed[1]))
    
    answer = [[]]
    installed = [[], []] # [0]: 기둥  [1]: 보
    for x, y, a, b in build_frame:
        if b == 0: # 삭제
            if a == 0: # 기둥 삭제
                installed[0].remove([x,y])
                if (([x, y+1] in installed[0] and check0(x, y+1) == False)
                        or ([x-1,y+1] in installed[1] and check1(x-1,y+1) == False)
                        or ([x, y+1] in installed[1] and check1(x, y+1) == False) ):
                    installed[0].append([x,y]) # 복구
            else: # 보 삭제
                installed[1].remove([x,y])
                if(([x-1,y] in installed[1] and check1(x-1,y) == False)
                        or ([x+1,y] in installed[1] and check1(x+1,y) == False)
                        or ([x,y] in installed[0] and check0(x,y) == False)
                        or ([x+1,y] in installed[0] and check0(x+1,y) == False)):               
                    installed[1].append([x,y]) # 복구
        else: # 설치
            if a == 0: # 기둥 설치
                if check0(x,y):
                    installed[0].append([x,y])
            else: # 보 설치
                if check1(x,y):
                    installed[1].append([x,y])
    answer = [[x[0], x[1], 0] for x in installed[0]] + [[x[0], x[1], 1] for x in installed[1]]
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    return answer