basic_operator = ['+', '-', '*']

def calculator(a, b, p):
    if p == '*':
        return a * b
    if p == '+':
        return a + b
    return a - b


def make_priority(index, priority, visited, temp):
    if index == 3:
        priority.append(temp[:])
        return

    for i in range(3):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(basic_operator[i])
            make_priority(index + 1, priority, visited, temp)
            temp.pop()
            visited[i] = 0


def solution(expression):
    answer = 0
    numbers = []
    formula = []
    slice_index = 0

    for i in range(len(expression)):
        if expression[i] in basic_operator:
            numbers.append(int(expression[slice_index:i]))
            formula.append(expression[i])
            slice_index = i + 1

    numbers.append(int(expression[slice_index:]))
    priority = []
    visited = [0, 0, 0]
    make_priority(0, priority, visited, [])

    for val in priority:
        temp_numbers = numbers[:]
        temp_formula = formula[:]
        for p in val:
            i = 0
            while (i < len(temp_formula)):
                if temp_formula[i] == p:
                    a = temp_numbers[i]
                    b = temp_numbers.pop(i + 1)
                    temp_numbers[i] = calculator(a, b, p)
                    temp_formula.pop(i)
                    i -= 1
                i += 1
        if abs(temp_numbers[0]) > answer:
            answer = abs(temp_numbers[0])
    return answer
