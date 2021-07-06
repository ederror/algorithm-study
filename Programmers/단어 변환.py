# Programmers - 단어 변환
def diff(str1, str2): 
    # len(str1) == len(str2)
    length = len(str1)
    cnt = 0
    for i in range(length):
        if str1[i] == str2[i]:
            cnt += 1
    return (length - cnt)
        
def solution(begin, target, words):

    visited = [0 for _ in range(len(words))]
    q = []
    q.append(begin)
    
    # BFS
    while q:
        v = q.pop(0) # current word
        
        for w in range(len(words)):
            
            if visited[w] == 0 and diff(v, words[w]) == 1:
                q.append(words[w])
                
                if v == begin:
                    visited[w] = 1
                else:
                    visited[w] = visited[words.index(v)] + 1
                
                # if found
                if words[w] == target:
                     return visited[w]
            
    return 0