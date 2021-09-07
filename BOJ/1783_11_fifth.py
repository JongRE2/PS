# 병든 나이트 (X)

n, m = map(int,input().split())

if n == 1 or m == 1:
    cnt = 1
elif m >= 7:
    if n >= 4:
        cnt = 3 + (m-1)
    else:
