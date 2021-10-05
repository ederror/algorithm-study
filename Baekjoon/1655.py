# Baekjoon - 1655
import sys
import heapq

input = sys.stdin.readline

N = int(input())
maxheap = [] # left
minheap = [] # right
for i in range(N):
    x = int(input())
    if i % 2 == 0:
        heapq.heappush(maxheap, -x)
        print(-minheap[0])
    else:
        heapq.heappush(minheap, x)
        if -maxheap[0] < minheap[0]:
            print(-maxheap[0])
        else:
            print(minheap[0])
