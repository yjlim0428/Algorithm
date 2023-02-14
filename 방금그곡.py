# def timeCarculator(start, end):
#     startHour, startMinute = map(int, start.split(":"))
#     endHour, endMinute = map(int, end.split(":"))
#     return (endHour * 60 + endMinute) - (startHour * 60 + startMinute)
#
# def playMelody(time, melody):
#     if time == len(melody):
#         return melody
#     if time < len(melody):
#         return melody[:time + 1]
#     else:
#         shap = (melody * time)[:time + 1].count("#")  # 샾이 들어간 갯수
#         result = (melody * time)[:time + 2 + shap]
#         if result[-1] != "#":
#             return result[:len(result) - 1]
#         return result
#
# def solution(m, musicinfos):
#     result = "(None)"  # 결과 반환 값
#     musicTimeMin = 0 # 재생 시간 비교
#     for i in musicinfos:
#         start, end, title, melody = i.split(',')
#         musicTime = timeCarculator(start, end)  # 재생 시간 값 구하기
#         melody = playMelody(musicTime, melody)   # 재생된 멜로디 구하기
#         if m not in melody:
#             continue
#         else:
#             if m+"#" not in melody:
#                 if musicTimeMin < musicTime:
#                     result = title
#                     musicTimeMin = musicTime
#
#     return result
#

###########################################################################

def timeCarculator(start, end):
    startHour, startMinute = map(int, start.split(":"))
    endHour, endMinute = map(int, end.split(":"))
    return (endHour * 60 + endMinute) - (startHour * 60 + startMinute)

def playMelody(time, melody):
    if time == len(melody):
        return melody
    if time < len(melody):
        return melody[:time + 1]
    else:
        return (melody * time)[:time + 1]



def changeShap(string):
    replaceDic = {"C#": "z", "D#": "y", "F#": "x", "G#": "w", "A#": "v"}
    for k in replaceDic.keys():
        string = string.replace(k, replaceDic[k])
    return string

def solution(m, musicinfos):
    result = "(None)"  # 결과 반환 값
    musicTimeMin = 0 # 재생 시간 비교

    for i in musicinfos:
        start, end, title, melody = i.split(',')
        musicTime = timeCarculator(start, end)  # 재생 시간 값 구하기
        melody = playMelody(musicTime, changeShap(melody))   # 재생된 멜로디 구하기
        if changeShap(m) not in melody:
            continue
        else:
            if musicTimeMin < musicTime:
                result = title
                musicTimeMin = musicTime

    return result






print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))