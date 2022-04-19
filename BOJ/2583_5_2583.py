## 영역구하기

from collections import deque

m, n, k = map(int,input().split())
chk = [[0]*n for _ in range(m)]

cnt = list()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(k):
    x, y, xx, yy = map(int, input().split())

    for i in range(y, yy):
        for j in range(x, xx):
            chk[i][j] = 1


dq = deque()

for i in range(m):
    for j in range(n):
        if chk[i][j] == 0:
            chk[i][j] = 1
            count = 1
            dq.append((j, i))
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]

                    if 0 <= yy < m and 0 <= xx < n and chk[yy][xx] == 0:
                        chk[yy][xx] = 1
                        count += 1
                        dq.append((xx,yy))

            cnt.append(count)

print(len(cnt))
cnt.sort()

for val in cnt:
    print(val, end = ' ')





