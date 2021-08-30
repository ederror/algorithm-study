# Programmers - 무지의 먹방 라이브
def solution(food_times, k):
    answer = 0
    ftcopy = [e for e in food_times]
    food_times.sort(reverse= True)
    eaten = 0
    while food_times:
        food = food_times[-1]
        if (food-eaten)*len(food_times) <= k:
            k -= (food-eaten)*len(food_times)
            eaten = food
            food_times.pop()
        else:
            break
    
    if not food_times:
        return -1

    k = k % len(food_times) +1
    for i, food in enumerate(ftcopy):
        if food-eaten <= 0:
            continue
        k -= 1
        if k <= 0:
            return i+1
    return -1