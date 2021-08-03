# Baekjoon - 4803
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(v):
    visited.append(v)
    tree[treeID].append(v)
    for w in graph[v]:
        if w not in visited:
            DFS(w)
     
n, m = 1, 1
tc = 1
while True:
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    
    treeID = 0
    numOfTree = 0
    graph = [[] for _ in range(n+1)]
    tree = [[] for _ in range(n)]
    visited = []
    
    for _ in range(m):
        v, w = map(int, input().split())
        graph[v].append(w)
    
    for v in range(1,n+1):
        if v not in visited:
            DFS(v)
            
            numOfEdge = 0
            for w in tree[treeID]:
                numOfEdge += len(graph[w])
            
            if numOfEdge == len(tree[treeID])-1:
                numOfTree += 1
                
            treeID += 1
    
    print(f'Case {tc}: ', end="")
    
    if numOfTree == 1:
        print("There is one tree.")
    elif numOfTree == 0:
        print("No trees.")
    else:
        print(f'A forest of {numOfTree} trees.')
        
    tc += 1