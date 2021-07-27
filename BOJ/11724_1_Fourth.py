# 연결요소의 갯수
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n, m = map(int,input().split())
node_cn = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())
    node_cn[u][v] = True
    node_cn[v][u] = True

node_chk = [False]*(n+1)


cnt = 0

def dfs(prsnt):
    for next in range(1,n+1):
        if node_cn[prsnt][next] and (node_chk[next] == False):
            node_chk[next] = True
            dfs(next)

for i in range(1, n+1):
    if node_chk[i] == False:
        cnt += 1
        node_chk[i] = True
        dfs(i)
print(cnt)

