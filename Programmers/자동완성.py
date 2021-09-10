# Programmers - 자동완성
def solution(words):
    class Trie():
        def __init__(self):
            self.exist = False
            self.child = {}
            self.cnt = 0

        def insert(self, data):
            cur = self
            for c in data:
                cur.cnt += 1
                if c not in cur.child:
                    cur.child[c] = Trie()
                cur = cur.child[c]
            cur.exist = True
            cur.cnt += 1

        def find(self, data):
            cur = self
            ret = 0
            for c in data:
                if c not in cur.child:
                    return 0
                if cur.cnt > 1:
                    ret += 1
                cur = cur.child[c]
                
            if cur.exist:
                return ret
            else:
                return 0

    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    for word in words:
        answer += trie.find(word)
    return answer