# Baekjoon - 11725
n = int(input())
tree = [[] for _ in range(n+1)]
q = [1] # queue for BFS
visited = [0] * (n+1)

for _ in range(n-1):
    v, w = map(int, input().split())
    tree[w].append(v)
    tree[v].append(w)

# BFS
while q:
    v = q.pop(0)
    for w in tree[v]:
        if visited[w] == 0:
            visited[w] = v # parent
            q.append(w)

for v in visited[2:]:
    print(v)