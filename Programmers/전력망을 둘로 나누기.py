# Programmers - 전력망을 둘로 나누기
def solution(n, wires):
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        parent[y] = x
        
    answer = -1

    for exclusive in range(len(wires)):
        parent = [i for i in range(n)]
        for i, (v1, v2) in enumerate(wires):
            if i == exclusive:
                continue
            union(v1-1, v2-1)
        root = find(0)
        cnt1, cnt2 = 1, 0
        for v in range(1,n):
            if find(v) == root:
                cnt1 += 1
            else:
                cnt2 += 1
        if answer == -1 or answer > abs(cnt1 - cnt2):
            answer = abs(cnt1 - cnt2)

    return answer