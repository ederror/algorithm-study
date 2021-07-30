# Baekjoon - 5693
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def get_postorder(s, e):    
    if s > e:
        return
    
    root = preorder[s]
    idx = s+1
    while idx <= e:
        if root < preorder[idx]:
            break
        idx += 1
    
    get_postorder(s+1, idx-1)
    get_postorder(idx, e)
    
    print(root)
    
preorder = [] # VLR
while True:
    try:
        preorder.append(int(input()))
    except:
        break
get_postorder(0, len(preorder)-1)