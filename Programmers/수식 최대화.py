# Programmers - 수식 최대화
import itertools

def solution(expression):
    answer = 0
    priority = list(itertools.permutations(['+', '-', '*'], 3))

    expressionSplit = []
    # split
    i = 0
    while i < len(expression):
        j = i
        while j < len(expression) and expression[j] not in ['+', '-', '*']:
            j += 1
        expressionSplit.append(int(expression[i:j]))
        i = j+1
        if i < len(expression):
            expressionSplit.append(expression[j])
    
    for p in priority:
        expList = [i for i in expressionSplit] # copy
        for operation in p:
            while True:
                try:
                    i = expList.index(operation)
                except:
                    break
                op1 = expList.pop(i-1)
                expList.pop(i-1) # + or - or *
                op2 = expList.pop(i-1)
                res = 0
                if operation == '+':
                    res = op1+op2
                elif operation == '-':
                    res = op1-op2
                elif operation == '*':
                    res = op1*op2
                
                expList.insert(i-1, res)
        answer = max(answer, abs(expList[0]))
    return answer