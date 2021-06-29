from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_length = len(weak)

    for i in range(weak_length):
        weak.append(weak[i] + n)

    dist_cases = list(map(list,permutations(dist,len(dist))))

    for i in range(weak_length):
        start = [weak[j] for j in range(i, i + weak_length)]
        for dist_each in dist_cases:
            dist_distance = 0
            result = 1
            check_len = start[0] +dist_each[0]

            for k in range(weak_length):
                if start[k] > check_len:
                    result += 1
                    if result > len(dist_each):
                        break
                    dist_distance += 1
                    check_len = start[k] + dist_each[dist_distance]
            answer = min(answer,result)
    if answer > len(dist):
        return -1
    return answer


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n, weak, dist))