# 베스트 셀러

num = int(input())

books = dict()

for _ in range(num):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_val = max(books.values())

arr =list()

for k,v in books.items():
    if v == max_val:
        arr.append(k)

arr.sort()

print(arr[0])