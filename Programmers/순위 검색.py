# Programmers - 순위 검색
def solution(info, query):
    answer = []
    info = [x.split() for x in info]
    #info.sort(key = lambda x: int(x[4]))

    dic = {}
    for app in info:
        for i in [app[0], '-']:
            for j in [app[1], '-']:
                for k in [app[2], '-']:
                    for l in [app[3], '-']:
                        key = i+j+k+l
                        if key in dic:
                            dic[key].append(int(app[4]))
                        else:
                            dic[key] = [int(app[4])]
                            
    for key in dic:
        dic[key].sort()
        
    for q in query:
        q = q.split()
        key = q[0]+q[2]+q[4]+q[6]
        target = int(q[-1])
        if key in dic: # 코딩 테스트 점수 조사
            # under-bound
            points = dic[key]
            s, e = 0, len(points)
            while s < e:
                m = (s+e) // 2
                if points[m] < target:
                    s = m+1
                else:
                    e = m
            answer.append(len(points) - s)
        else:
            answer.append(0)

    return answer