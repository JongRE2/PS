# 절대값 힙


import sys, heapq

input = sys.stdin.readline

plus = []
minus = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(minus)>0:
            if len(plus)>0:
                if minus[0] <= plus[0]:
                    print(-heapq.heappop(minus))
                else:
                    print(heapq.heappop(plus))
            else: #len(plus) <= 0 일때
                print(-heapq.heappop(minus))
        elif len(plus)>0:
            print(heapq.heappop(plus))
        else:
            print(0)

    else:
        if x > 0:
            heapq.heappush(plus,x)
        else:
            heapq.heappush(minus,-x)





