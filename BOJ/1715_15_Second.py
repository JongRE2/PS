# 카드 정렬하기
import sys,heapq
input = sys.stdin.readline
num = int(input())
cards = []

sum = 0

for _ in range(num):
    heapq.heappush(cards,int(input()))

if len(cards) == 1:
    print(0)

else:
    while len(cards) > 1:
        temp1 = heapq.heappop(cards)
        temp2 = heapq.heappop(cards)
        sum += (temp1 + temp2)
        heapq.heappush(cards,temp1 + temp2)

    print(sum)