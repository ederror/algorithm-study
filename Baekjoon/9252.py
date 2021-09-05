# Baekjoon - 9252
import sys
input = sys.stdin.readline

seq1 = input().rstrip()
seq2 = input().rstrip()

dp = [[0 for __ in range(len(seq2))] for __ in range(len(seq1))]

for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        else:
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])

answer = []
i, j = len(seq1)-1, len(seq2)-1
print(dp[i][j])

while i >= 0 and j >= 0:
    if seq1[i] == seq2[j]:
        answer.append(seq1[i])
        i -= 1
        j -= 1
    else:
        a, b = -1, -1
        if i > 0:
            a = dp[i-1][j]
        if j > 0:
            b = dp[i][j-1]
        if a > b:
            i -= 1
        else:
            j -= 1
for a in answer[::-1]:
    print(a, end= "")