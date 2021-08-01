# 큐2
import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
deq = deque()

for _ in range(num):
    stc = list(map(str,input().split()))
    if stc[0] == 'push':
        deq.append(stc[1]) # 출력값 X
    elif stc[0] == 'pop':
        if len(deq):
            print(deq.popleft())
        else:
            print("-1")
    elif stc[0] == 'size':
        print(len(deq))
    elif stc[0] == 'empty':
        if len(deq):
            print("0")
        else:
            print("1")
    elif stc[0] == 'front':
        if len(deq):
            print(deq[0])
        else:
            print("-1")
    elif stc[0] == 'back':
        if len(deq):
            print(deq[-1])
        else:
            print("-1")