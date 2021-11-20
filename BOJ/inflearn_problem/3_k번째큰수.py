n, k = map(int, input().split())
arr = list(map(int, input().split()))
correcting = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            correcting.add(arr[i]+arr[j]+arr[m])

correcting = list(correcting)
correcting.sort(reverse=True)
print(correcting[k-1])

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# res = set()
#
# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             res.add(a[i] + a[j] + a[m])
# res = list(res)
# res.sort(reverse=True)
# print(res[k-1])
