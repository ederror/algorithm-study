# Baekjoon -1991
def preorder(node): # VLR
    global Btree
    print(node, end="")
    if Btree[node][0] != '.':
        preorder(Btree[node][0])
    if Btree[node][1] != '.':
        preorder(Btree[node][1])

def inorder(node): # LVR
    global Btree
    if Btree[node][0] != '.':
        inorder(Btree[node][0])
    print(node, end="")
    if Btree[node][1] != '.':
        inorder(Btree[node][1])

def postorder(node): # LRV
    global Btree
    if Btree[node][0] != '.':
        postorder(Btree[node][0])
    if Btree[node][1] != '.':
        postorder(Btree[node][1])
    print(node, end="")

n = int(input())
Btree = {}

for _ in range(n):
    parent, lchild, rchild = input().split()
    Btree[parent] = [lchild, rchild]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()