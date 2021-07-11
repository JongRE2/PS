# 숫자카드 2번째풀이
_ = int(input())
cards = set(map(int,input().split()))

_ = int(input())

ans = []
for a in list(map(int,input().split())):
    ans.append(1 if a in cards else 0)

print(' '.join(map(str,ans)))