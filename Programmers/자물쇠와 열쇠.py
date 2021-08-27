# Programmers - 자물쇠와 열쇠
def solution(key, lock):
    def rotate(arr): # 배열을 시계방향으로 90도 회전 후 반환
        return [[arr[row][col] for row in range(len(arr)-1, -1, -1)] for col in range(len(arr))]
    
    answer = True
    keys = [key]
    num = 0 # 자물쇠의 홈의 개수
    M, N = len(key) , len(lock)
    for l in lock:
        num += l.count(0)
        
    for __ in range(3):
        key = rotate(key)
        keys.append(key)
    
    for key in keys:
        for r in range(-(M-1), N):
            for c in range(-(M-1), N):
                cnt, flag = 0, True
                for i in range(M):
                    for j in range(M):
                        if not(0<=r+i<N and 0<=c+j<N):
                            continue
                            
                        if key[i][j] == 1 and lock[r+i][c+j] == 0:
                            cnt += 1
                        elif key[i][j] == 1 and lock[r+i][c+j] == 1:
                            flag = False
                            break
                if cnt == num and flag == True:
                    return True
    return False