# 풍선 터뜨리기

n = int(input())

data = list(map(int,input().split()))

index = [ x for x in range(1,n+1)]

idx = 0

position = data.pop(idx) # 제일 처음 빼는 애.

arr = list()
arr.append(index.pop(idx))

while data:
    if position < 0:
        idx = (idx + position) % len(data)
    else:
        idx = (idx + position -1) % len(data)
    position = data.pop(idx)
    arr.append(index.pop(idx))

for i in arr:
    print(i,end=' ')