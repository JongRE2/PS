dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())

arrList = list()

for _ in range(n):
    arr = list(map(int, input().split()))
    arr.append(0)
    arr.insert(0, 0)
    arrList.append(arr)


inputList = [0]*(n+2)
arrList.append(inputList)
arrList.insert(0, inputList)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(arrList[i][j] > arrList[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)


'''
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
'''
#     if arrList[i][j] <= arrList[i+dx[a]][j+dy[a]]:
#         chk = 1
# if chk == 0:
#     cnt += 1