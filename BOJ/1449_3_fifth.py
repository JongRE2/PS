# 1449 - 수리공 항승
#shift + alt + end: 색변함
N, L = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

end = arr[0] + L
cnt = 1
i = 1

while i < len(arr):
    if arr[i] < end:
        i += 1
        continue
    end = arr[i] + L
    i += 1
    cnt += 1

print(cnt)

# position = 0
# cnt = 0
#
# for a in arr:
#
#     if a < position:
#         continue
#     elif a >= position:
#         position = a + L
#         cnt += 1
#
# print(cnt)