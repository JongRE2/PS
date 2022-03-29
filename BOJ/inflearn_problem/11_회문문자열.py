n = int(input())

# def evalVal(str):

for i in range(1, n+1):
    str = input()
    str_len = len(str)

    for j in range(0, str_len // 2):
        if str[j].lower() != str[-(j+1)].lower():
            print(f'#{i} NO')
            break
    else:
        print(f'#{i} YES')


