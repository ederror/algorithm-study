# Baekjoon - 2263  : (실패) 메모리 초과
def findRoot(postorder, inorder):
    global tree
    if not postorder or not inorder:
        return 0
    root = postorder[-1]
    idx = inorder.index(root)
    lchild = findRoot(postorder[:idx], inorder[:idx])
    rchild = findRoot(postorder[idx:-1], inorder[idx+1:])
    tree[root] = [lchild, rchild]

    return root

def preorder(root):
    global tree
    if root == 0:
        return
    
    print(root, end=" ")
    preorder(tree[root][0]) # left child
    preorder(tree[root][1]) # right child

n = int(input())
inorder = list(map(int, input().split())) # LVR
postorder = list(map(int, input().split())) # LRV

tree = [[0, 0] for _ in range(n+1)]
preorder(findRoot(postorder, inorder))