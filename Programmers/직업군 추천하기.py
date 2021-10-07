# Programmers - 직업군 추천하기
def solution(table, languages, preference):
    points = [['SI', 0], ['CONTENTS', 0], ['HARDWARE', 0], ['PORTAL', 0], ['GAME', 0]]
    
    for i in range(len(table)):
        table[i] = table[i].split()
        for j in range(len(languages)):
            try:
                points[i][1] += (6 - table[i].index(languages[j])) * preference[j]
            except:
                continue
    points.sort(key=lambda x: (-x[1], x[0]))
        
    return points[0][0]