# Programmers - 메뉴 리뉴얼
from itertools import combinations
def solution(orders, course):
    answer = []
    menu = dict()
    for i, order in enumerate(orders):
        for m in order:
            if m not in menu:
                menu[m] = [i]
            else:
                menu[m].append(i)
        order = list(order)
        order.sort()
        orders[i] = "".join(order)

    for c_num in course:
        max = 1
        cand = []
        combination = set()
        for order in orders:
            if len(order) >= c_num:
                combination = combination | set(combinations(order, c_num))
        
        for comb in combination:
            tmpSet = set(menu[comb[0]])
            for m in comb:
                tmpSet = tmpSet & set(menu[m])
                if len(tmpSet) < max:
                    break
            comb = list(comb)
            comb.sort()
            
            if len(tmpSet) > max:
                max = len(tmpSet)
                cand = ["".join(comb)] # reset
            elif max >= 2 and len(tmpSet) == max:
                cand.append("".join(comb))
                
        answer.extend(cand)
    answer.sort()

    return answer