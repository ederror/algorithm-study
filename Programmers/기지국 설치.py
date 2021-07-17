# Programmers - 기지국 설치
import math
def solution(n, stations, w):
    answer = 0
    segments = []
    s = 1
    for station in stations:
        if station-w > s:
            segments.append([s, station-w-1])
        s = station+w+1
    if s <= n:
        segments.append([s, n])
    
    for seg in segments:
        answer += math.ceil((seg[1] - seg[0] + 1) / (2*w+1))
           
    return answer