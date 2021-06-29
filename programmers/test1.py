
answer = "123"
size = len(answer)
i = 0

val = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

while i < size:
    if answer[i] == 'z':
        if i + 4 >= size:
            answer = answer[:i] + '0'
        else:
            answer = answer[:i] + '0' + answer[i + 4:size]
    elif answer[i] == 'o':
        if i + 3 >= size:
            answer = answer[:i] + '1'
        else:
            answer = answer[:i] + '1' + answer[i + 3:size]
    elif answer[i] == 't':
        if answer[i + 1] == 'w':
            if i+3 >= size:
                answer = answer[:i] + '2'
            else:
                answer = answer[:i] + '2' + answer[i + 3:size]
        else:
            if i+5 >= size:
                answer = answer[:i] + '3'
            else:
                answer = answer[:i] + '3' + answer[i + 5:size]
    elif answer[i] == 'f':
        if answer[i + 1] == 'o':
            if i+4 >= size:
                answer = answer[:i] + '4'
            else:
                answer = answer[:i] + '4' + answer[i + 4:size]
        else:
            if i+4 >= size:
                answer = answer[:i] + '5'
            else:
                answer = answer[:i] + '5' + answer[i + 4:size]
    elif answer[i] == 's':
        if answer[i + 1] == 'i':
            if i+3 >= size:
                answer = answer[:i] + '6'
            else:
                answer = answer[:i] + '6' + answer[i + 3:size]
        else:
            if i+5 >= size:
                answer = answer[:i] + '7'
            else:
                answer = answer[:i] + '7' + answer[i + 5:size]
    elif answer[i] == 'e':
        if i+5 >= size:
            answer = answer[:i] + '8'
        else:
            answer = answer[:i] + '8' + answer[i + 5:size]

    elif answer[i] == 'n':
        if i+4 >= size:
            answer = answer[:i] + '9'
        else:
            answer = answer[:i] + '9' + answer[i + 4:size]
    i +=1
    size = len(answer)

print(answer)