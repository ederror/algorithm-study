# Programmers - 매칭 점수  sorry..
def solution(word, pages):
    answer = 0
    points = []
    linkpoints = []
    word = word.lower()
    linkDict = {}
    linkDictInv = {}
    pageUrl = []
    
    for page in pages:
        page = page.lower()
        point, idx = 0, -1
        while True:    # 기본점수 확인
            idx = page.find(word, idx+1)
            if idx == -1:
                break
            if idx+len(word) < len(page) and ord('a')<=ord(page[idx+len(word)])<=ord('z'):
                idx += len(word)
                continue
            
            point += 1
            idx += len(word)
            
        myUrl = ""
        idx = page.find('<meta property="og:url"')
        idx = page.find('http', idx)
        endIdx = page.find('"', idx)
        myUrl = page[idx:endIdx]
        pageUrl.append(myUrl)
        
        idx = -1
        while True: # 링크 수 확인
            idx = page.find('<a href', idx+1)
            if idx == -1:
                break
            idx += 9
            endIdx = page.find('"', idx)
            linkUrl = page[idx:endIdx]
            
            if myUrl not in linkDict:
                linkDict[myUrl] = []
            linkDict[myUrl].append(linkUrl) # myUrl -> linkUrl
            
            if linkUrl not in linkDictInv:
                linkDictInv[linkUrl] = []
            linkDictInv[linkUrl].append(myUrl)
            
        points.append(point)
    
    # 링크점수
    for url in pageUrl:
        point = 0
        if url not in linkDictInv:
            linkpoints.append(point)
            continue
        
        for link in linkDictInv[url]:
            try:
                idx = pageUrl.index(link)
                point += points[idx] / len(linkDict[link])
            except:
                continue
        
        linkpoints.append(point)
    points = [points[i] + linkpoints[i] for i in range(len(points))]
    
    maxP = -1
    for i, p in enumerate(points):
        if p > maxP:
            maxP = p
            answer = i
    
    return answer