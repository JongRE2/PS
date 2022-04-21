# 1991 - 트리 순회
import sys
input = sys.stdin.readline
n = int(input())
tree = {}

def preorder(root):
    if root != '.':
        print(root, end = '')
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])

def ineorder(root):
    if tree[root][0] != '.':
        ineorder(tree[root][0])
    if root != '.':
        print(root, end = '')
    if tree[root][1] != '.':
        ineorder(tree[root][1])

def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    if root != '.':
        print(root, end = '')


for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
preorder('A')
print()
ineorder('A')
print()
postorder('A')