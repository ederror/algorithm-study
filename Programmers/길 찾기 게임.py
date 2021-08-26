# Programmers - 길 찾기 게임
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    def findChildren(ninfo):
        if not ninfo:
            return -1
        
        root_x, root_y, root_idx = ninfo[0]
        
        # left 
        leftinfo = [info for info in ninfo if info[1] < root_y and info[0] < root_x]
        leftchild = findChildren(leftinfo)
        
        # right
        rightinfo = [info for info in ninfo if info[1] < root_y and info[0] > root_x]
        rightchild = findChildren(rightinfo)
        tree[root_idx] = [leftchild, rightchild]
        return root_idx
    
    def preorder(v): # VLR
        if v == -1:
            return
        answer[0].append(v) # visit
        preorder(tree[v][0]) # L
        preorder(tree[v][1]) # R
        
    def postorder(v): # LRV
        if v == -1:
            return
        postorder(tree[v][0])
        postorder(tree[v][1])
        answer[1].append(v)
        
        
    answer = [[],[]]
    tree = {i+1: [-1, -1] for i in range(len(nodeinfo))}
    
    # add node index to nodeinfo
    nodeinfo = [[nodeinfo[i][0], nodeinfo[i][1], i+1] for i in range(len(nodeinfo))]
    
    nodeinfo.sort(key = lambda x: (x[1], -x[0]), reverse= True)
    root = findChildren(nodeinfo)
    
    preorder(root)
    postorder(root)
    
    return answer