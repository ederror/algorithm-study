# Programmers - 셔틀버스
def solution(n, t, m, timetable):
    
    def toMinute(timestamp):
        return int(timestamp[:2])*60 + int(timestamp[3:])
    
    def toTimestamp(minute):
        hour = minute // 60
        minute = minute % 60
        return f'{hour:02}:{minute:02}'
    
    answer = 0
    firstShuttle = toMinute("09:00")
    waitQueue = {firstShuttle+i*t : [] for i in range(n)}
    
    timetable = [toMinute(i) for i in timetable]
    timetable.sort()
    
    for crew in timetable:
        for time in waitQueue: # 버스 도착 시간
            if crew <= time and len(waitQueue[time]) < m:
                waitQueue[time].append(crew)
                break
            
    lastShuttle = firstShuttle+(n-1)*t
    if len(waitQueue[lastShuttle]) < m: # 마지막 버스 줄이 꽉차지 않은 경우
        answer = lastShuttle
    else: # 줄이 꽉찬 경우 -> 마지막 사람보다 1분 빨리
        answer = waitQueue[lastShuttle][-1]-1
        
    return toTimestamp(answer)