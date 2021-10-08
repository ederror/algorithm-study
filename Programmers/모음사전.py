# Programmers - 모음사전
def solution(word):
    answer = 0
    alphabets = ['A', 'E', 'I', 'O', 'U']
    call_num = -1

    def dfs(cur_word):
        nonlocal call_num, answer
        call_num += 1
        if word == cur_word:
            answer = call_num
            return
        elif len(cur_word) == 5:
            return
        else:
            for alphabet in alphabets:
                dfs(cur_word + alphabet)
                
    dfs('')
    return answer