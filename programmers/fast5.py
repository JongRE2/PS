import re

def solution(words, queries):
    answer = []

    for query_word in queries:
        count = 0
        edited_word = query_word.replace("?", ".")
        print(edited_word,len(edited_word))
        for each_word in words:
            if len(query_word) == len(each_word):
                result = re.search(edited_word, each_word)
                if result != None:
                    count += 1
        answer.append(count)

    return answer



words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))