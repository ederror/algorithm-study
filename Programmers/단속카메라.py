# Programmers - 단속카메라
def solution(routes):
    routes.sort(key = lambda x : x[0])
    answer = 1
    camera = routes[0][1]
    for route in routes[1:]:
        # 현재 route가 단속 범위에 포함
        if route[0] <= camera:
            camera = min(route[1], camera)    
        else: # 새로운 카메라
            camera = route[1]
            answer += 1
    return answer