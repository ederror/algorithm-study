# Baekjoon - 1016
import sys
import math
input = sys.stdin.readline

isprime = [1]*1000000
prime = []
for i in range(2, 1000000):
    if isprime[i] == 1:
        prime.append(i*i)
        for j in range(i*2, 1000000, i):
            isprime[j] = 0

min_, max_ = map(int, input().split())

isnono = [1] * (max_ - min_ + 1)

for p in prime:
    if p > max_:
        break
    
    tmp = int(math.ceil(min_ / p)) * p
    for i in range(tmp, max_+1, p):
        isnono[i-min_] = 0

print(sum(isnono))