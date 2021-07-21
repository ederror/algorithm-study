# Programmers - 줄 서는 방법
def solution(n, k):
    answer = []
    factorial = [1, 1]
    number = list(range(1,n+1)) # 숫자 중복 사용 방지
    
    for i in range(2, n): # factorial 미리 계산
        factorial.append(factorial[i-1] * i)
    
    k -= 1
    for i in range(n):
        idx = k // factorial[n-1-i]
        answer.append(number.pop(idx))
        k %= factorial[n-1-i] 
    
    return answer