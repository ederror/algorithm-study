# Programmers - 불량 사용자
def solution(user_id, banned_id):
    def backTrack(caseList, i):
        if i == len(banned_id):
            caseList.sort()
            for ans in answer: # 중복 확인
                if ans == caseList:
                    return
            answer.append(caseList) # 중복 없으면 답에 추가
            return

        for x in candidates[i]:
            if x not in caseList:
                caseList.append(x)
                caseListCopy = [i for i in caseList]
                backTrack(caseListCopy, i+1)
                caseList.pop()
    
    answer = []
    candidates = []
    for bid in banned_id:
        candidate = []
        for uid in user_id:
            if len(bid) != len(uid):
                continue
            
            flag = True
            for i in range(len(bid)):
                if bid[i] != '*' and uid[i] != bid[i]:
                    flag = False
                    break
            
            if flag:
                candidate.append(uid)
        candidates.append(candidate)

    backTrack([], 0)
    
    return len(answer)