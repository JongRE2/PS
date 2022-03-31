from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)
cnt = 0
while arr:
    if len(arr) == 1:
        arr.pop()
        cnt += 1
    if arr[0] + arr[-1] > m:
        arr.pop()
        cnt += 1
    else:
        arr.popleft()
        arr.pop()
        cnt += 1

print(cnt)
'''
5 140
90 50 70 100 60
'''