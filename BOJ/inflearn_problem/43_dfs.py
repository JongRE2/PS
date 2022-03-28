## 부분집합 구하기
n = int(input())

chk = [0]*(n+1)


def dfs(v):
    if v == n+1:
        for i in range(0, n):
            if chk[i]:
                print(i+1, end = ' ')
        print()
    else:
        chk[v-1] = 1
        dfs(v+1)
        chk[v-1] = 0
        dfs(v+1)
dfs(1)