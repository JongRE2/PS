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
# def digit_sum(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum

#내 풀이
n = int(input())

arr = list(map(int, input().split()))

sumarr=list()
def digit_sum(x):
    remain = 0
    sumval = 0
    if x == 0:
        return 0
    else:
        while x > 0:
            sumval += (x % 10)
            x = x // 10
        return sumval

for a in arr:
    sumarr.append(digit_sum(a))

print(arr[sumarr.index(max(sumarr))])