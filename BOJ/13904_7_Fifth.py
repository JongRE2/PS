## 과제
from collections import deque
import sys
import heapq
input = sys.stdin.readline

num = int(input())

check = [0]*1000

datas = []

for i in range(num):
    day, score = map(int,input().split())
    datas.append([-score, day])
heapq.heapify(datas)


for _ in range(num):

    if len(datas) != 0:
        score, day = heapq.heappop(datas)
        # print(score, day)
    else:
        break
    if check[day-1] == 0:
        check[day-1] = -score
    else:
        index = 1
        while check[day-1-index] != 0 and day-1-index >= 0:
            index += 1
        if day-1-index >= 0 and check[day-1-index] == 0:
            check[day - 1 - index] = -score
print(sum(check))




















# arr = list()
# arr = list()
# for i in range(num):
#     day, score = map(int, input().split())
#     arr.append((score, day))
#
# arr.sort(reverse=True)
# arr2 = deque(arr)
#
# sum = 0
#
# for i in range(0, num):
#     if len(arr2) > 0:
#         x, y = arr2.popleft()
#     else:
#         break
#     while y-i < 0:
#         if len(arr2) > 0:
#             x, y = arr2.popleft()
#         else:
#             break
#     # print(f'합하게 되는 score값 : {x}')
#     sum += x
# print(sum)















