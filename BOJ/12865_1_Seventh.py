# 평범한배낭
n, k = map(int,input().split())

best_store = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        best_store[i][j] = best_store[i-1][j]
        if j >= w:
            best_store[i][j] = max(best_store[i][j], best_store[i-1][j-w] + v)

print(best_store[n][k])