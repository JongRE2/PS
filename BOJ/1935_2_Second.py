# 후의표기식2

N = int(input())

expression = input()

val = []
stk = []
for _ in range(N):
    val.append(int(input()))


for ch in expression:
    if ch == '+':
        b = stk.pop()
        a = stk.pop()
        stk.append(a+b)
    elif ch == '-':
        b = stk.pop()
        a = stk.pop()
        stk.append(a-b)
    elif ch == '*':
        b = stk.pop()
        a = stk.pop()
        stk.append(a*b)
    elif ch == '/':
        b = stk.pop()
        a = stk.pop()
        stk.append(a/b)
    else:
        stk.append(val[ord(ch)-ord('A')])

print(f'{stk.pop():.2f}')

