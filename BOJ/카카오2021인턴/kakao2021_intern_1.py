# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    global arr
    answer = ""
    i = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            answer += s[i]
            i += 1
            continue
        else:
            for key, value in arr.items():
                if s[i:(i+2)] in key:
                    i += len(key)
                    answer += value
                    break
    return int(answer)

arr = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
