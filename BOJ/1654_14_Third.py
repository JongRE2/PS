# 랜선 자르기

k,n = map(int,input().split())
Line = []

res = 0

Line = [int(input()) for _ in range(k)]
largest = max(Line)

# print(Line)
val = 0
lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    sum = 0
    for i in Line:
        sum = sum + (i//mid)
    if sum >= n:
        lt = mid+1
        val = mid
    else:
        rt = mid-1

print(val)
