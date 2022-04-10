n = int(input())

arr = list(map(int, input().split()))
score = [0]*n

chck = 0
val = 1
for i in range(0, n):

    if arr[i] == 1:
        if chck == 0:
            score[i] = val
            chck = 1
        elif chck == 1:
            val += 1
            score[i] = val
    elif arr[i] == 0:
        chck = 0
        val = 1
        score[i] = 0

print(sum(score))

