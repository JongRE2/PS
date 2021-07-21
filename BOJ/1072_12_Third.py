# 게임
x,y = map(int,input().split())
z = y*100 // x

answer = 0

if z >= 99:
    answer = -1


else:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        sum = (y+mid)*100 // (x+mid)
        if sum <= z:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
print(answer)

