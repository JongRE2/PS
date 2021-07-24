## 분해법


n = int(input())
global val
for i in range(1,1000001):
    val = i
    chk = False
    sum = 0
    sum += i
    mul = 1
    # print('------',i,'---------------')
    while i != 0:
        remain = (i % 10)
        i = i // 10
        sum += remain
    # print('---끝--',sum,',',n,i)
    if sum == n:
        chk = True
        break
if chk == True:
    print(val)
else:
    print(0)


