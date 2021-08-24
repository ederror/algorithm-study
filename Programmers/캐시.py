# Programmers - 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        
        if city not in cache: # Cache miss
            answer += 5 
            if len(cache) < cacheSize:
                cache.append(city)
            elif cacheSize != 0:
                cache.pop(0)
                cache.append(city)
        else: # Cache hit
            answer += 1
            cache.remove(city)
            cache.append(city)
            
    return answer