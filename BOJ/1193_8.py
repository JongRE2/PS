# 분수 찾기

val = int(input())
line = 0
total_val = 0

while val > total_val:
    line += 1
    total_val += line

gap = total_val - val
if line % 2 != 0:
    top = gap + 1
    down = line - gap
else:
    top = line - gap
    down = gap + 1

print(f'{top}/{down}')





# https://ooyoung.tistory.com/84
