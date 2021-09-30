# Programmers - 상호평가
def solution(scores):
    answer = ''
    for student in range(len(scores)):
        onlyMin, onlyMax = True, True
        score = [s[student] for s in scores] # 자신이 받은 점수
        
        for st, sc in enumerate(score):
            if st == student:
                continue
            if sc >= score[student]:
                onlyMax = False
            if sc <= score[student]:
                onlyMin = False
                
        avg = 0  
        sum_ = sum(score)
        if onlyMin or onlyMax:
            avg = (sum_ - score[student]) / (len(scores) - 1)
        else:
            avg = sum_ / len(scores)
            
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer