# Baekjoon - 1167_2
def DFS(v):
    global tree, n, visited
    
    for edge in tree[v]:
        w, cost = edge[0], edge[1]
        if visited[w] == -1:
            visited[w] = visited[v] + cost
            DFS(w)
    
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n):
    inputLst = list(map(int, input().split()))
    v = inputLst[0]
    for i in range(1, len(inputLst)-1, 2):
        tree[v].append([inputLst[i], inputLst[i+1]])

maxNode, maxDist = 0, 0
visited = [-1] * (n+1)
visited[1] = 0
DFS(1)

v = visited.index(max(visited))
visited = [-1] * (n+1)
visited[v] = 0
DFS(v)

print(max(visited))