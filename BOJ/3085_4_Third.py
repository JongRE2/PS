# 사탕게임
num = int(input())

square = [list(input()) for _ in range(num)]
ans = 1

def search1(y, x):
    global ans
    for i in range(x,x+2):
        if i < num:
            cnt = 1
            for j in range(1,num):
                if square[j-1][i] == square[j][i]:
                    cnt += 1
                    ans = max(ans,cnt)
                else:
                    cnt = 1

    for i in range(y,y+2):
        if i < num:
            cnt = 1
            for j in range(1,num):
                if square[i][j-1] == square[i][j]:
                    cnt += 1
                    ans = max(ans,cnt)
                else:
                    cnt = 1


for i in range(num):
    for j in range(num):
        if j + 1 < num:
            square[i][j],square[i][j+1] = square[i][j+1],square[i][j]
            search1(i,j)
            square[i][j], square[i][j + 1] = square[i][j + 1], square[i][j]
        if i + 1 < num:
            square[i][j],square[i+1][j] = square[i+1][j],square[i][j]
            search1(i,j)
            square[i][j], square[i + 1][j] = square[i + 1][j], square[i][j]

print(ans)