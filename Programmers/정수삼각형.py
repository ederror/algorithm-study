# Programmers - 정수삼각형
def solution(triangle):
    answer = 0
    height = len(triangle)
    
    # triangle의 각 원소를 '거쳐간 숫자의 최댓값'으로 업데이트
    for h in range(1, height):
        triangle[h][0] += triangle[h-1][0]
        
        for i in range(1, h):
            triangle[h][i] += max(triangle[h-1][i], triangle[h-1][i-1])
        
        triangle[h][h] += triangle[h-1][h-1]
    
    # 가장 밑단의 최댓값
    answer = max(triangle[height-1])
    return answer