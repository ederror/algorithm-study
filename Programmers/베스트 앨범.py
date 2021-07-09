# Programmers - 베스트 앨범
def solution(genres, plays):
    answer = []
    genreCount = []
    music = {}
    i = 0
    for genre in genres:
        if genre not in music:
            music[genre] = [plays[i], i]
        else:
            idx = 1
            for musicIdx in music[genre][1:]:
                if plays[musicIdx] < plays[i]:
                    break
                idx += 1
            music[genre].insert(idx, i)
            music[genre][0] += plays[i]
        i += 1
        
    for genre in music:
        genreCount.append([music[genre][0], genre])
        
    genreCount.sort(reverse = True)
    
    for gc in genreCount:
        genre  = gc[1]
        
        i = 0
        for musicIdx in music[genre][1:]:
            answer.append(musicIdx)
            i += 1
            if i == 2:
                break
            
    return answer