# Programmers - 파일명 정렬
def solution(files):
    answer = []
    fileinfo = []
    for file in files:
        hidx = 0
        for c in file:
            if ord('0')<=ord(c)<=ord('9'):
                break
            else:
                hidx += 1
                
        head = file[:hidx]
        nidx = hidx
        for c in file[hidx:]:
            if ord('0')<=ord(c)<=ord('9'):
                nidx += 1
            else:
                break
        
        number = file[hidx:nidx]
        tail = file[nidx:]
        
        fileinfo.append([head, number, tail])
        
    fileinfo.sort(key= lambda x: (x[0].lower(), int(x[1])))
    for info in fileinfo:
        answer.append("".join(info))
    return answer