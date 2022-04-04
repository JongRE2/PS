# 틀린 내 풀이
# import sys
# sys.setrecursionlimit(100000)
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
#
# cnt = 0
#
# for lt in range(n):
#     sum = 0
#     sum = arr[lt]
#     rt = lt
#     while lt <= rt and rt < n:
#         if lt == rt:
#             if sum == m:
#                 cnt += 1
#                 break
#             else:
#                 rt += 1
#         else:
#             sum += arr[rt]
#             if sum == m:
#                 cnt += 1
#                 break
#             elif sum < m:
#                 rt += 1
#             else:
#                 break
# print(cnt)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = 1
totals = arr[0]
cnt = 0
while True:
    if totals < m:
        if rt < n:
            totals += arr[rt]
            rt += 1
        else:
            break
    elif totals == m:
        cnt += 1
        totals -= arr[lt]
        lt += 1


# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# lt = 0
# rt = 1
# tot = arr[0]
# cnt = 0
# while True:
#     if tot < m:
#         if rt < n:
#             tot += arr[rt]
#             rt += 1
#         else:
#             break
#     elif tot == m:
#         cnt += 1
#         tot -= arr[lt]
#         lt += 1
#     else:
#         tot -= arr[lt]
#         lt += 1
#
# print(cnt)












