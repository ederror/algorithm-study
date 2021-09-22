# Baekjoon - 14891
import sys
input = sys.stdin.readline

gear = [input() for _ in range(4)]
north = [0]*4
K = int(input())
for __ in range(K):
    idx, d = map(int, input().split())
    rotate = [0]*4
    idx -= 1
    rotate[idx] = d

    # 왼쪽에 있는 톱니바퀴들
    for i in range(idx-1, -1, -1):
        # 오른쪽 톱니바퀴(i+1)의 서쪽과 자신의 동쪽 비교
        if gear[i+1][(north[i+1]-2) % 8] != gear[i][(north[i]+2) % 8]:
            rotate[i] = rotate[i+1] * -1

    # 오른쪽에 있는 톱니바퀴들
    for i in range(idx+1, 4):
        # 왼쪽 톱니바퀴(i-1)의 동쪽과 자신의 서쪽 비교
        if gear[i-1][(north[i-1]+2) % 8] != gear[i][(north[i]-2) % 8]:
            rotate[i] = rotate[i-1] * -1

    # 회전
    for i in range(4):
        north[i] = (north[i] - rotate[i]) % 8
print(sum([(2**i) * int(gear[i][north[i]]) for i in range(4)]))