## 카드2
from collections import deque

N = int(input())
arr = deque()

for i in range(1,N+1):
    arr.append(i)

while True:
    arr.popleft()
    if len(arr) == 1:
        break
    arr.append(arr.popleft())


print(arr[0])
