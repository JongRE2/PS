# 브론즈1 : 달팽이는 올라가고 싶다
# 구글링 참고함.

a,b,v = map(int,input().split())
day = 1

day = (v - b) / (a - b)
print(int(day) if day == int(day) else int(day) + 1)
