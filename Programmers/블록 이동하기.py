# Programmers - 블록 이동하기
def solution(board):
    answer = 0
    N = len(board)
    status = 0 # 0 : 가로   1 : 세로
    queue = [[0, 0, status]]
    visited = {(0, 0, status) : 1}
    while queue:
        x, y, status = queue.pop(0)
        if (x==N-2 and y==N-1 and status==0) \
                or (x==N-1 and y==N-2 and status==1):
            break
        cur_dist = visited[(x,y,status)]
        if status == 0:
            if x+2<N and board[x+2][y] == 0 \
                    and (x+2, y, status) not in visited:
                queue.append([x+2,y,status])
                visited[(x+2,y,status)] = cur_dist+1
            if x-1>=0 and board[x-1][y] == 0 \
                    and (x-1, y, status) not in visited:
                queue.append([[x-1,y,status]])
                visited[(x-1,y,status)] = cur_dist+1
            if y+1<N and board[x][y+1] == 0 and board[x+1][y+1] == 0:
                if (x,y,1) not in visited:
                    queue.append([x,y,1])
                    visited[(x,y,1)] = cur_dist+1
                if (x+1,y,1) not in visited:
                    queue.append([x+1,y,1])
                    visited[(x+1,y,1)] = cur_dist+1
                    
        else:
            if y+2<N and board[x][y+2] == 0 \
                    and (x,y+2,status) not in visited:
                queue.append([x,y+2,status])
                visited[(x,y+2,status)] = cur_dist+1
            if y-1>=0 and board[x][y-1] == 0 \
                    and (x,y-1,status) not in visited:
                queue.append([x,y-1,status])
                visited[(x,y-1,status)] = cur_dist+1
            if x+1<N and board[x+1][y] == 0 and board[x+1][y+1] == 0:
                if (x,y,0) not in visited:
                    queue.append([x,y,0])
                    visited[(x,y,0)] = cur_dist+1
                if (x,y+1,0) not in visited:
                    queue.append([x,y+1,0])
                    visited[(x,y+1,0)] = cur_dist+1
                    
    print(visited)
    return answer
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))