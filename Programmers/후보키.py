# Programmers - 후보키
from itertools import combinations
def solution(relation):
    nCol = len(relation[0]) # num of column
    nRow = len(relation) # num of row
    candidate = []
    
    for i in range(1,nCol+1):
        for case in combinations(range(nCol), i):
            li = [tuple([row[col] for col in case]) for row in relation]
            
            if len(set(li)) == nRow:
                for c in candidate:
                    if set(c).issubset(set(case)):
                        break
                else: 
                    candidate.append(case)
                    
    return len(candidate)