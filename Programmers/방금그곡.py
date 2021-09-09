# Programmers - 방금그곡
def solution(m, musicinfos):
    def replaceSharp(string):
        string = string.replace("C#", "H")
        string = string.replace("D#", "I")
        string = string.replace("F#", "J")
        string = string.replace("G#", "K")
        string = string.replace("A#", "L")
        return string
    
    def toMinute(timestamp):
        return int(timestamp[:2])*60 + int(timestamp[3:])

    answer = '(None)'
    answer_duration = 0
    m = replaceSharp(m)
    
    for musicinfo in musicinfos:
        start_time, end_time, music_name, melody = musicinfo.split(',')
        start_time = toMinute(start_time)
        end_time = toMinute(end_time)
        melody = replaceSharp(melody)
        duration = end_time - start_time
        
        entire_melody = melody * (duration // len(melody)) + melody[:(duration % len(melody))]
        
        if entire_melody.find(m) != -1:
            if answer_duration < duration:
                answer = music_name
                answer_duration = duration
    return answer