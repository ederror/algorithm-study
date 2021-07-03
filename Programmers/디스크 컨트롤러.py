# Programmers - 디스크 컨트롤러
def solution(jobs):
    answer = 0
    numOfJobs = len(jobs)
    clk = 0
    jobs.sort(key = lambda x:(x[0] , -x[1]))

    # Shortest Job First (non-preemptive)
    while jobs:
        minIdx = 0
        flag = 0
        for jobIdx in range(len(jobs)):
            # 요청이 들어온 job 중 소요 시간 최소인 job
            if jobs[jobIdx][0] <= clk and jobs[jobIdx][1] <= jobs[minIdx][1]:
                minIdx = jobIdx
                flag = 1
        
        if flag == 1: # 조건 만족하는 Job이 하나라도 있는 경우
            startClk, duration = jobs.pop(minIdx)
            clk += duration # 실행시간
            answer += clk - startClk # 반환시간
        else: # 조건 만족하는 job 없는 경우 -> clk만 1 증가
            clk += 1
    return answer // numOfJobs