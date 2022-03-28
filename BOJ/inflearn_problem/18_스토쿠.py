arr = list(list(map(int, input().split())) for _ in range(9))

'''
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
'''
def checkVal(arr):
    mark = 0
    for i in range(9):
        check1 = [0] * 10
        check2 = [0] * 10
        for j in range(9):
            if check1[arr[i][j]] == 0:
                check1[arr[i][j]] += 1
            else:
                return False
            if check2[arr[j][i]] == 0:
                check2[arr[j][i]] += 1
            else:
                return False
    for a in range(3):
        for b in range(3):
            check3 = [0] * 10
            for c in range(3):
                for d in range(3):
                    check3[arr[a * 3 + c][b * 3 + d]] = 1
            if sum(check3) != 9:
                return False
    return True


if checkVal(arr):
    print("YES")
else:
    print("NO")
