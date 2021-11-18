T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    arr.sort()
    print("#%d %d" % (t + 1, arr[k - 1]))


















# T = int(input())
#
# for t in range(T):
#     N, s, e, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     a = a[s-1:e]
#     a.sort()
#     print("#%d %d" %(t+1, a[k-1]))
