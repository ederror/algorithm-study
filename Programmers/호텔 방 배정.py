# Programmers - 호텔 방 배정
import sys
sys.setrecursionlimit(10**6)
def solution(k, room_number):
    
    def find(x):
        if x not in emptyRoom:
            return x
        emptyRoom[x] = find(emptyRoom[x])
        return emptyRoom[x]
    
    answer = []
    emptyRoom = dict()
    
    for room in room_number:
        allocated = find(room)
        answer.append(allocated)
        if allocated < k:
            emptyRoom[allocated] = find(allocated+1)
        
    return answer