# Programmers - 여행 경로
def solution(tickets):
    answer = []
    airport = {}
    for a, b in tickets:
        if a not in airport:
            airport[a] = [b]
        else:
            airport[a].append(b)
        airport[a].sort()
    
    #print(airport)
    stack = ['ICN']
    # DFS
    
    
    while stack:
        print(stack, airport)
        top = stack[-1]
        if top not in airport or not airport[top]:
            answer.append(stack.pop())
        else:
            stack.append(airport[top].pop(0))
    
    
    return answer[::-1]