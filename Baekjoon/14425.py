# Baekjoon - 14425
import sys

input = sys.stdin.readline

class Trie():
    def __init__(self):
        self.exist = False
        self.child = {}

    def insert(self, data):
        cur = self
        for c in data:
            if c not in cur.child:
                cur.child[c] = Trie()
            cur = cur.child[c]
        cur.exist = True

    def find(self, data):
        cur = self
        for c in data:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        if cur.exist:
            return True
        else:
            return False

answer = 0
N, M = map(int, input().split())
S = Trie()

for _ in range(N):
    S.insert(input())

for _ in range(M):
    s = input()
    if S.find(s):
        answer += 1
print(answer)