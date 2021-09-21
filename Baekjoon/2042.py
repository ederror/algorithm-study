# Baekjoon - 2042
import sys
from collections import defaultdict
input = sys.stdin.readline

def makeSegtree(v, start, end):
    if start == end:
        segTree[v] = seq[start]
        return segTree[v]
    
    mid = (start + end) // 2
    segTree[v] = makeSegtree(2*v, start, mid) + makeSegtree(2*v+1, mid+1, end)
    return segTree[v]

def updateSegtree(v, start, end, b, c): 
    if not (start <= b <= end):
        return
    
    segTree[v] = segTree[v] - seq[b] + c
    if start == end:
        return
    mid = (start + end) // 2
    updateSegtree(v*2, start, mid, b, c)
    updateSegtree(v*2+1, mid+1, end, b, c)

def getSum(v, start, end, l, r):
    if (l > end or r < start):
        return 0

    if (l <= start and end <= r): 
        return segTree[v]
    else: 
        mid = (start+end) // 2
        return getSum(v*2, start, mid, l, r) + getSum(v*2+1, mid+1, end, l, r)

N, M, K = map(int, input().split())
seq = []
segTree = defaultdict(int)

for __ in range(N):
    seq.append(int(input()))

makeSegtree(1, 0, N-1)
for __ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        updateSegtree(1, 0, N-1, b-1, c)
        seq[b-1] = c
    else:
        print(getSum(1, 0, N-1, b-1, c-1))