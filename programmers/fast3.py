def solution(array, commands):
    answer = []
    for arr in commands:
        start,end,index = arr
        copy_arr = array[start-1:end]
        copy_arr.sort()
        answer.append(copy_arr[index-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
