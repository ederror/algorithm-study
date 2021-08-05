# Baekjoon - 4195
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]

testcase = int(input())
for tc in range(testcase):
    f = int(input())
    id = {} # dictionary  (id["name"] = 번호)
    curID = 0
    parent = [i for i in range(f*2)]
    rank = [1] * (f*2)
    for _ in range(f):
        id1, id2 = input().split()
        if id1 not in id: # 처음 나온 id면 id번호(curID) 할당
            id[id1] = curID
            curID += 1
        if id2 not in id:
            id[id2] = curID
            curID += 1
        
        if find(id[id1]) != find(id[id2]): # 연결 되어있지 않다면
            union(id[id1], id[id2])
        print(rank[find(id[id1])]) # 결과 출력