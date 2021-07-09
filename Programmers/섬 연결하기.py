# Programmers - 섬 연결하기
def solution(n, costs):
    
    costs.sort(key = lambda x : x[2])
    
    selectedNode = [costs[0][0], costs[0][1]]
    answer = costs[0][2]
    
    # Prim
    while len(selectedNode) != n:
        for edge in costs:
            if edge[0] in selectedNode or edge[1] in selectedNode:
                
                # Cycle 생성되는 경우
                if edge[0] in selectedNode and edge[1] in selectedNode:
                    continue
                
                if edge[0] in selectedNode:
                    selectedNode.append(edge[1])
                else:
                    selectedNode.append(edge[0])
                
                answer += edge[2]
                break
        
    return answer