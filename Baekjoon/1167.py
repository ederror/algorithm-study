# Baekjoon - 1167 (BFS) => 시간 초과
def BFS(startNode):
    global tree, n
    q = [startNode]
    visited = [-1] * (n+1) 
    visited[startNode] = 0
    maxNode, maxDist = 0, -1

    while q:
        v = q.pop(0)
        for edge in tree[v]:
            w, weight = edge[0], edge[1]
            if visited[w] == -1: # not visited yet
                visited[w] = visited[v] + weight # store the distance from startNode
                q.append(w)
                if visited[w] > maxDist:
                    maxDist = visited[w]
                    maxNode = w
    
    # startNode에서 가장 먼 노드와 거리를 반환
    return maxNode, maxDist

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n):
    inputLst = list(map(int, input().split()))
    v = inputLst[0]
    for i in range(1, len(inputLst)-1, 2):
        tree[v].append([inputLst[i], inputLst[i+1]])
    
v, _ = BFS(1)
_, dist = BFS(v)
print(dist)