# 숫자 정사각형

y, x = map(int, input().split())

arr = [list(map(int, input())) for _ in range(y)]
std = y if y < x else x

# print(std)
# for i in range(y):
#     print(arr[i])
val_most = 0
for i in range(y):
    for j in range(x):
        for k in range(std):
            if i+k < y and j+k < x:
                if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                    val_most = (k+1)*(k+1) if val_most < (k+1)*(k+1) else val_most
print(val_most)
