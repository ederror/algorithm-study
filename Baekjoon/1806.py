# Baekjoon - 1806
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

s, e = 0, 0
answer = N+1
partialSum = seq[0]
while s<=e and e < N:
    
    if partialSum < S:
        e += 1
        try:
            partialSum += seq[e]
        except:
            break
    elif partialSum > S:
        answer = min(answer, e-s+1)
        partialSum -= seq[s]
        s += 1
    else:
        answer = min(answer, e-s+1)
        e += 1
        try:
            partialSum += seq[e]
        except:
            break

if answer > N:
    answer = 0
print(answer)