# 2003 - 수들의 합2

n, m = map(int, input().split())
n = n-1
arr = list(map(int, input().split()))


i, j = 0, 0
cnt = 0

while j <= n:
    sum = 0
    if i == j:
        sum = arr[i]
    else:
        for x in range(i, j + 1):
            sum += arr[x]

    if sum < m:
        j += 1
    elif sum == m:
        cnt += 1
        if i != n:
            i += 1
            j += 1
        else:
            break
    elif sum > m:
        if i < j:
            i += 1
        else:
            i += 1
            j += 1

print(cnt)

