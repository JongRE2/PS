## 2212-센서
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

position = list(map(int,input().split()))

position.sort()
diff = list()
if k >= n:
    print(0)
else:
    for i in range(1, n):
        diff.append(position[i] - position[i-1])
    diff.sort(reverse=True)

    for _ in range(k - 1):
        diff.pop(0)

    print(sum(diff))


