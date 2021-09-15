# 행렬
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

matrix_a = [list(map(int, input().rstrip())) for _ in range(n)]
result_matrix_a = [list(map(int, input().rstrip())) for _ in range(n)]


def converted(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix_a[i][j] = 1 - matrix_a[i][j]
cnt = 0

for x in range(n-2):
    for y in range(m-2):
        if matrix_a[x][y] == result_matrix_a[x][y]:
            continue
        else:
            cnt += 1
            converted(x, y)

flag = 0
for i in range(n):
    for j in range(m):
        if matrix_a[i][j] != result_matrix_a[i][j]:
            flag = 1
            break

if flag == 1:
    print(-1)
else:
    print(cnt)



