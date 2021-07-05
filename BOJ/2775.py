# 2775_ 부녀회장이 될테야
case = int(input())
sum = 0

for i in range(case):
    k = int(input())
    n = int(input())
    floor0 = [x for x in range(0,n+2)]
    for i in range(k):
        for j in range(1,n+1):
            floor0[j] += floor0[j-1]
    print(floor0[n])