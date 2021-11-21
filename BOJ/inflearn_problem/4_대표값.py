n = int(input())
arr = list(map(int, input().split()))
arr_avg = int(sum(arr) / len(arr) + 0.5)

val_min = 2147000000
for idx, val in enumerate(arr):
    if abs(arr_avg-val) < val_min:
        val_min = abs(arr_avg-val)
        score = val
        order = idx + 1
    elif abs(arr_avg-val) == val_min:
        if score < val:
            score = val
            order = idx + 1

print("%d %d" % (arr_avg, order))
