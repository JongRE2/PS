import sys
input = sys.stdin.readline


def dfs(level, total):
    global c, max_sum

    if c < total:
        return

    if level == n:
        max_sum = max(max_sum, total)
        return





    dfs(level + 1, total + arr[level])
    dfs(level + 1, total)


c, n = map(int, input().split())
chk = [0] * n
max_sum = -1

arr = [int(input()) for _ in range(n)]

dfs(0, 0)
print(max_sum)


