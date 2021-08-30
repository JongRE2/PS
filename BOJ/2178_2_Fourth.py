# 2178 - 미로탐색
import sys
sys.setrecursionlimit(10 ** 8)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

global cann_min

def dfs(x, y, cnt):
    global cann_min
    cnt += 1
    if x == n-1 and y == m-1:
        cann_min = cnt if cann_min > cnt else cann_min
    else:
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and board[x + dx[i]][y + dy[i]] == 1:
                board[x + dx[i]][y + dy[i]] = 0
                dfs(x + dx[i], y + dy[i], cnt)
                board[x + dx[i]][y + dy[i]] = 1
    return


n, m = map(int,input().split())


cann_min = 100*(n+m)
cnt = 0
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        board[i][j] = int(board[i][j])
dfs(0, 0, cnt)

print(cann_min)