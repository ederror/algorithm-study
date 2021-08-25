# Programmers - 오픈채팅방
def solution(record):
    answer = []
    mapping = {}
    tmp = [] # ['E' or 'L' , uid] 저장
    
    for line in record:
        line = line.split()
        if line[0] == "Enter":
            mapping[line[1]] = line[2]
            tmp.append(["E", line[1]])
        elif line[0] == "Leave":
            tmp.append(["L", line[1]])
        elif line[0] == "Change":
            mapping[line[1]] = line[2]
            
    for line in tmp:
        if line[0] == "E": # Enter
            answer.append(f'{mapping[line[1]]}님이 들어왔습니다.')
        else: # Leave
            answer.append(f'{mapping[line[1]]}님이 나갔습니다.')
    return answer