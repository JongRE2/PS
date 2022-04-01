num, m = map(int, input().split())
num = map(int, str(num))
strings = list()

for a in num:
    while strings and m > 0 and strings[-1] < a:
        strings.pop()
        m -= 1
    strings.append(a)

while m > 0:
    strings.pop()
    m -= 1

stc = ''
for a in strings:
    stc += str(a)
print(stc)

''' 
5276823 3
'''