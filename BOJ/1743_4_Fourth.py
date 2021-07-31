# 1743 음식물쓰레기

import sys
from collections import deque


input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m,k = map(int, (input().split()))

board = [[0] * m for _ in range(n)]

chk = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int,input().split())
    board[r-1][c-1] = 1

dq = deque()

def bfs(y, x):
    global cnt
    dq.append((y, x))
    chk[y][x] = 1
    cnt += 1

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0 <= yy < n and 0 <= xx < m and chk[yy][xx] == 0 and board[yy][xx] == 1:
                dq.append((yy,xx))
                chk[yy][xx] = 1
                cnt += 1


max_cnt = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            bfs(i, j)
            max_cnt = max(max_cnt, cnt)
            cnt = 0

print(max_cnt)




