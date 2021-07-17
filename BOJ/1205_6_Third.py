# 등수구하기
n,new_score,p = map(int,input().split())

str = -1

if n != 0:
    arr = list(map(int, input().split()))

    if n == p and arr[-1] >= new_score:
        str = -1
    else:
        for i in range(n):
            if arr[i] <= new_score:
                str = i+1
                break
        if str == -1 and n < p:
            str = len(arr)+1
else:
    str = 1
print(str)


