# 숫자카드 1번쨰 풀이
from bisect import bisect_left,bisect_right


num1 = int(input())
arr1 = sorted(list(map(int,input().split())))

num2 = int(input())
arr2 = list(map(int,input().split()))

arr3 = []
for i in range(num2):
    val = bisect_right(arr1,arr2[i])-bisect_left(arr1,arr2[i])

    if val > 0:
        arr3.append(1)
    else:
        arr3.append(0)
print(' '.join(map(str,arr3)))