# Programmers - 가사 검색
def solution(words, queries):
    class Trie():
        def __init__(self, level):
            self.child = {}
            self.count = {} # item = (len: 개수)
            self.level = level
        
        def insert(self, string):
            cur = self
            length = len(string)
            for c in string:
                if c not in cur.child:
                    cur.child[c] = Trie(self.level+1)
                cur = cur.child[c]
                if length not in cur.count:
                    cur.count[length] = 1
                else:
                    cur.count[length] += 1
        
        def search(self, string, length):
            cur = self
            if not string: # ?만 있는 경우
                cnt = 0
                for c in cur.child.values():
                    if length in c.count:
                        cnt += c.count[length]
                return cnt
            
            for c in string:
                if c not in cur.child:
                    return 0
                cur = cur.child[c]
            if length in cur.count:
                return cur.count[length]
            else:
                return 0   
        
    answer = []
    lTrie = Trie(0)
    rTrie = Trie(0)
    
    for word in words:
        lTrie.insert(word)
        rTrie.insert(word[::-1])
    
    for query in queries:
        length = len(query)
        if query[0] == '?': # ??abc
            query = query.lstrip('?')[::-1]
            answer.append(rTrie.search(query, length))
            
        elif query[-1] == '?': # abc??
            query = query.rstrip('?')
            answer.append(lTrie.search(query, length))
            
    return answer