# N번째 큰수

import sys,heapq

input = sys.stdin.readline

pq = []
num = int(input())

for _ in range(num):
    pq.append(list(map(int,input().split())))

arr = []
heapq.heapify(arr)

for i in range(num):
    for j in range(num):
        heapq.heappush(arr,pq[i][j])

    for _ in range(num*num,num,-1):
        print(heapq.heappop(arr))

print(heapq.heappop(arr))
