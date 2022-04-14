n = int(input())

arr = list()

def sum_val(a, chk):
    rtn_val = -1
    for i in range(1,len(chk)):
        if chk[i] == a:
            rtn_val = i
    return rtn_val

for i in range(n):
    chk = [0]*7
    max_val = -2147000000
    max_chk = -1
    a = list(map(int, input().split()))
    for idx, val in enumerate(a):
        chk[val] += 1
        if max_val < val:
            max_val = val

    if max(chk) == 3:
        arr.append(10000+(sum_val(3, chk))*1000)
    elif max(chk) == 2:
        arr.append(1000 + (sum_val(2, chk)) * 100)
    else:
        arr.append(max_val*100)
arr.sort(reverse=True)
print(arr[0])

# 나의 새로운 풀이
# n = int(input())
#
# total_prize = 0
# max_prize = 0
# for _ in range(n):
#     arr = [0] * 7
#     x, y, z = map(int, input().split())
#     arr[x] += 1
#     arr[y] += 1
#     arr[z] += 1
#     zerocnt = 0
#     severalval = -1
#     for i in range(1, 7):
#         if arr[i] == 0:
#             zerocnt += 1
#         else:
#             if arr[i] > 1:
#                 severalval = i
#     if zerocnt == 3:
#         total_prize = max(arr)*100
#     elif zerocnt == 4:
#         total_prize = 1000 + (severalval)*100
#     elif zerocnt == 5:
#         total_prize = 10000 + (severalval) * 1000
#     if max_prize < total_prize:
#         max_prize = total_prize
# print(max_prize)
