# Programmers - 신규 아이디 추천
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for c in new_id:
        if ord('0')<=ord(c)<=ord('9') or ord('a')<=ord(c)<=ord('z') or c in ['-', '_', '.']:
            if len(answer) != 0 and c == '.' and answer[-1] == '.':
                continue
            answer += c
            
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
        
    if not answer:
        answer = "a"
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    
    tmp = answer[-1]
    while len(answer) <= 2:
        answer += tmp
        
    return answer