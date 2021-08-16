# 4153 - 직각삼각형
while True:
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    arr = list()
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.sort()
    a = arr.pop(); b = arr.pop(); c = arr.pop()
    if a*a == b*b + c*cㄴ:
        print('right')
    else:
        print('wrong')

