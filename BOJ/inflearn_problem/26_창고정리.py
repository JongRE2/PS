l = int(input())

arr = list(map(int, input().split()))

m = int(input())
# arr.sort()
for _ in range(m):
    arr.sort()
    arr[0] += 1
    arr[l-1] -= 1

arr.sort()
print(arr[l-1] - arr[0])

'''
10
69 42 68 76 40 87 14 65 76 81
50
'''