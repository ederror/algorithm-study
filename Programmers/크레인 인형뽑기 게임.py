# Programmers - 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        move -= 1
        cur = -1
        for i in range(len(board)):
            if board[i][move] != 0:
                cur = board[i][move]
                board[i][move] = 0
                break
        
        if cur != -1:
            basket.append(cur)
            
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
                      
    return answer