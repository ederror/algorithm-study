# Baekjoon - 14725
import sys
input = sys.stdin.readline
N = int(input())

class Tree():
    def __init__(self, data, level):
        self.child = []
        self.data = data
        self.level = level

    def insert(self, data):
        """ 현재 tree의 자식으로 tree_node를 삽입 
            삽입 후 해당 노드 포인터 반환
        """
        for c in self.child:
            if c.data == data:
                return c
            
        node = Tree(data, self.level+1)
        self.child.append(node)
        self.child.sort(key = lambda x: x.data)
        return node
    
    def print_preorder(self):
        if self.data != None:
            for __ in range(self.level-1):
                print("--", end="")
            print(self.data)
        for c in self.child:
            c.print_preorder()

tree = Tree(None, 0)
for _ in range(N):
    line = list(input().split())
    K, data = int(line[0]), line[1:]
    curNode = tree
    for d in data:
        curNode = curNode.insert(d)

tree.print_preorder()