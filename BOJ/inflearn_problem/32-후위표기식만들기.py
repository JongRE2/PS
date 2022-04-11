n = input()

str_space = ''
stack = list()
for a in n:

    if a.isdecimal():
        str_space += a

    if a == '*' or a == '/':
        if stack and (stack[-1] == '*' or stack[-1] == '/'):
            str_space += stack.pop()
        stack.append(a)
    elif a == '+' or a == '-':
        while stack and stack[-1] != '(':
            str_space += stack.pop()
        stack.append(a)
    elif a == ')':
        while stack and stack[-1] != '(':
            str_space += stack.pop()
        stack.pop()
    elif a == '(':
        stack.append(a)

while stack:
    str_space += stack.pop()
print(str_space)


'''
3+5*2/(7-2)
'''