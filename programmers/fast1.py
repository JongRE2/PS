def solution(s):
    reverse_s = s[::-1]
    if s == reverse_s :
        return ''
    else:
        length = len(s) // 2
        reverse_ss = s[:length]
        return s[:length] + reverse_ss[::-1]


s = 'wabe'
print(solution(s))
