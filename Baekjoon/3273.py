# Baekjoon - 3273
import sys
input = sys.stdin.readline

answer = 0 
n = int(input())
seq = list(map(int, input().split()))
x = int(input())

seq.sort()
s, e = 0, n-1
while s < e and s < n and e >= 0:
    curValue = seq[s] + seq[e]
    
    if curValue == x:
        answer += 1
        s += 1
        e -= 1
    elif curValue > x:
        e -= 1
    else:
        s += 1
print(answer)