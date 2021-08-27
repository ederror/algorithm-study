# Programmers - 괄호 변환
def solution(p):
    def correct(p):
        if p == '':
            return p
        
        u, newp = '', ''
        idx, cnt = 0, 0
        stack = [] # to check if u is correct
        for c in p:
            idx += 1
            if c == '(':
                cnt += 1
                stack.append(c)
            elif c == ')':
                cnt -= 1
                if stack and stack[-1] == '(':
                    stack.pop()
                
            if cnt == 0:
                u = p[:idx]
                break
        v = correct(p[idx:])
        if stack: # u is not correct
            newp = '(' + v + ')'
            for c in u[1:-1]:
                if c == '(':
                    newp += ')'
                else:
                    newp += '('
        else:
            newp = u + v
        return newp
    
    return correct(p)