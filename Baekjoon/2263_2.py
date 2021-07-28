# Baekjoon - 2263 
def findRoot(post_s, post_e, inord_s, inord_e):
    global tree, postorder, inorder

    root = postorder[post_e-1]
    idx = inorder.index(root)
    lchild, rchild = 0, 0

    if inord_s != idx:
        lchild = findRoot(post_s, post_s + (idx-inord_s), inord_s, idx)

    if inord_e != idx+1:
        rchild = findRoot(post_s + (idx-inord_s), post_e-1, idx+1, inord_e)
   
    tree[root] = [lchild, rchild]

    return root

def preorder(root):
    global tree
    
    print(root, end=" ")
    if tree[root][0] != 0:
        preorder(tree[root][0]) # left child
    if tree[root][1] != 0:
        preorder(tree[root][1]) # right child

n = int(input())
inorder = list(map(int, input().split())) # LVR
postorder = list(map(int, input().split())) # LRV

tree = [[0, 0] for _ in range(n+1)]
preorder(findRoot(0, len(postorder), 0, len(inorder)))