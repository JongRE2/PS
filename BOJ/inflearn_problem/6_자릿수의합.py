# 내풀이
# def digit_sum(x):
#     sum = 0
#     while x != 0:
  #         sum += (x % 10)
#         x = (x // 10)
#     return sum
#
# n = int(input())
#
# max_val = -2147000000
# max_index = 0
# arr = list(map(int, input().split()))
#
# for idx, val in enumerate(arr):
#     if max_val < digit_sum(val):
#         max_val = digit_sum(val)
#         max_index = val
#
# print(max_index)

# 강사 풀이
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum
