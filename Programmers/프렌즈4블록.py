# Programmers - 프렌즈4블록
def solution(m, n, board):
    answer = 0
    board = [[board[j][i] for j in range(m)] for i in range(n)] # n x m
    
    while True:
        toBeDeleted = set([])
        
        for i in range(n-1):
            for j in range(m-1):
                if (board[i][j:j+2]+board[i+1][j:j+2]).count(board[i][j]) == 4 and board[i][j] != "X":
                    toBeDeleted.update([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])
                
        if not toBeDeleted:
            break
            
        answer += len(toBeDeleted)
        
        for i, j in toBeDeleted:
            board[i][j] = 'X'
        
        for i in range(n): # column
            j = len(board[i])-1
            for __ in range(m):
                if board[i][j] == 'X':
                    for k in range(j-1, -1, -1):
                        board[i][k+1] = board[i][k]
                    board[i][0] = 'X'
                else:
                    j -= 1
                    
    return answer