# Programmers - 풍선 터뜨리기
def solution(a):
    
    if len(a) <= 2:
        return len(a)
    
    answer = 2
    
    # leftMin[i] = a[:i] 의 최솟값
    leftMin = [0 for _ in range(len(a))]
    rightMin = [0 for _ in range(len(a))]
    
    # 가질 수 있는 최댓값으로 초기화
    leftMinValue = 1000000001
    rightMinValue = 1000000001
    
    for i in range(len(a)):
        j = len(a)-1-i
        
        if a[i] < leftMinValue:
            leftMinValue = a[i]
        if a[j] < rightMinValue:
            rightMinValue = a[j]
            
        leftMin[i] = leftMinValue
        rightMin[j] = rightMinValue

    for x in enumerate(a[1:-1]):
        balloon = x[1]
        idx = x[0]+1
        # 해당 풍선의 왼쪽, 오른쪽 부분 모두에 자신보다 작은 수가 있는 경우는 마지막까지 남지 못함
        if balloon == leftMin[idx] or balloon == rightMin[idx]:
            answer += 1

    return answer