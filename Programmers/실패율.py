# Programmers - 실패율
def solution(N, stages):
    fail = [[] for __ in range(N)]
    
    for curStage in range(1, N+1):
        cnt = len([stage for stage in stages if stage == curStage])
        acc = len([stage for stage in stages if stage >= curStage])
        try:
            fail[curStage-1] = [cnt/acc, curStage]
        except:
            fail[curStage-1] = [0, curStage]
        
    fail.sort(key = lambda x:x[0], reverse=True)
    return [fail[i][1] for i in range(N)]