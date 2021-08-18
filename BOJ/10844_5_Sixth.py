# 10844 쉬운계단수
n = int(input())

arr = [[0]*(n+1) for _ in range(10)]

for i in range(1, 10):
    arr[i][1] = 1

for i in range(2, n+1):
    for j in range(10):
        if j > 0:
            arr[j][i] += arr[j - 1][i - 1]
        if j < 9:
            arr[j][i] += arr[j + 1][i - 1]

total = 0
for i in range(10):
    total += arr[i][n]

print(total % 1000000000)
