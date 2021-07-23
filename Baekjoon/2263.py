# Baekjoon - 2263
def findRoot(postorder, inorder):
    global tree
    root = postorder[-1]
    idx = inorder.index(root)
    
    findRoot(, inorder[:idx])
    findRoot(, inorder[idx+1:])


n = int(input())
inorder = list(map(int, input().split())) # LVR
postorder = list(map(int, input().split())) # LRV

tree = [[] for _ in range(n+1)]
