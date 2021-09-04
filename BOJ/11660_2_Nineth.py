# 11660 - 구간합 구하기5
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# for _ in range(n):
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr[0][1])
acc = [[0]*n for _ in range(n)]
acc[0][0] = arr[0][0]

for x in range(1, n):
    acc[0][x] = acc[0][x-1] + arr[0][x]

for y in range(1, n):
    acc[y][0] = acc[y-1][0] + arr[y][0]
    for x in range(1, n):
        acc[y][x] = acc[y][x-1] + acc[y-1][x] - acc[y-1][x-1] + arr[y][x]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    wanted_val = acc[x2-1][y2-1]

    if (y1-2) >= 0:
        wanted_val -= acc[x2-1][y1-2]
    if (x1-2) >= 0:
        wanted_val -= acc[x1-2][y2-1]
    if x1-2 >= 0 and y1-2 >= 0:
        wanted_val += acc[x1 - 2][y1 - 2]
    print(wanted_val)