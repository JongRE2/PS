# import sys
# sys.setrecursionlimit(10 ** 6)
#
# def Find_maxval(arr,mid,max_sum1):
#     sum = 0
#     for i in arr:
#         if i < mid:
#             sum += i
#         else:
#             sum += mid
#     if Find_maxval(arr,(mid+max(arr)) // 2,max_sum1) <= max_sum1 and sum < Find_maxval(arr,(mid+max(arr)) // 2,max_sum1):
#         sum = Find_maxval(arr,(mid+max(arr)) // 2,max_sum1)
#     if Find_maxval(arr, (1 + mid) // 2, max_sum1) <= max_sum1 and sum < Find_maxval(arr, (1 + mid) // 2, max_sum1) <= max_sum1:
#         sum = Find_maxval(arr, (mid + max(arr)) // 2, max_sum1)
#
#     return sum

def is_possible(val):
    sum = 0
    for i in arr:
        sum += min(i,val)
    if max_sum < sum:
        return False
    return True

num = int(input()) # 첫줄
arr = list(map(int,input().split())) # 두번째줄
max_sum = int(input()) # 3번째줄

selected_mid = 0
l = 1
r = max(arr) + 1
mid = (l + (r-l)) // 2

while l < r:
    if is_possible(mid):
        selected_mid = max(selected_mid, mid)
        l = mid + 1
    else:
        r = mid
    mid = l + (r-l)//2

print(selected_mid)
