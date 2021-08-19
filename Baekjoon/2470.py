# Baekjoon - 2470
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
seq.sort()

s, e = 0, N-1
nearest = abs(seq[s] + seq[e])
answer = [s, e]
while s < e:
    curValue = seq[s] + seq[e]
    if nearest > abs(curValue):
        nearest = abs(curValue)
        answer[0], answer[1] = s, e
    
    if curValue > 0:
        e -= 1
    elif curValue < 0:
        s += 1
    else:
        break
print(seq[answer[0]], seq[answer[1]])