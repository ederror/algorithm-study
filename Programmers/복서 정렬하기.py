# Programmers - 복서 정렬하기
def solution(weights, head2head):
    key_list = []
    for i in range(len(weights)):
        key_comp = []
        num_compete = 0
        num_win = 0
        num_win_heavy = 0
        for j in range(len(weights)):
            if head2head[i][j] != 'N':
                num_compete += 1

            if head2head[i][j] == 'W':
                num_win += 1
                if weights[j] > weights[i]:
                    num_win_heavy += 1
        
        if num_compete == 0:
            key_comp = [0, 0]
        else:
            key_comp.append(num_win / num_compete)
            key_comp.append(num_win_heavy)
            
        key_comp.extend([weights[i], i])
        key_list.append(key_comp)
    key_list.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    
    return [x[3]+1 for x in key_list]