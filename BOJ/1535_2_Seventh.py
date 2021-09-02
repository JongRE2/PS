# 1535 안녕
import sys
input = sys.stdin.readline

n = int(input())
lossed = list(map(int,input().split()))
happy = list(map(int,input().split()))
dp = [[0]*101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        if j < lossed[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lossed[i-1]] + happy[i-1])

print(dp[n][99])
