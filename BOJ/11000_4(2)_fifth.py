# 11000 - 강의실 배정 

import sys,heapq

input = sys.stdin.readline

n = int(input())

arr = list()

for i in range(n):
    x, y = map(int,input().split())
    arr.append((x,y))

arr.sort()

rooms = list()

heapq.heappush(rooms, arr[0][1])

for i in range(1,n):
    x = arr[i][0]
    y = arr[i][1]
    if rooms[0] <= x:
        heapq.heappop(rooms)
        heapq.heappush(rooms, y)
    else:
        heapq.heappush(rooms, y)

print(len(rooms))