# 11659 구간합구하기4
import sys
input =sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
acc = [arr[0]]

for i in range(1, n):
    acc.append(acc[i-1] + arr[i])

for _ in range(m):
    i, j = map(lambda x:x-1, map(int, input().split()))
    # print(f'체크 = j값 : [{j}] / i값 : [{i}]  ||  {acc[j]} - {acc[i-1]}')
    # if i <= 0:
    #     print(acc[j])
    # else:
    #     print(acc[j] - acc[i - 1])
    print(acc[j] - (acc[i-1] if i else 0))
