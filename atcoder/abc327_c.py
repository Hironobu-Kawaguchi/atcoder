# https://atcoder.jp/contests/abc327/tasks/abc327_c

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

A = [list(map(int, input().split())) for _ in range(9)]
# print(A)

def chek(lst):
    cnt = [0] * 9
    for n in lst:
        cnt[n-1] += 1
    for n in cnt:
        if n != 1:
            return False
    return True

for i in range(9):
    lst = []
    for j in range(9):
        lst.append(A[i][j])
    if not chek(lst):
        print('No')
        exit()

for j in range(9):
    lst = []
    for i in range(9):
        lst.append(A[i][j])
    if not chek(lst):
        print('No')
        exit()

for si in range(0, 9, 3):
    for sj in range(0, 9, 3):
        lst = []
        for i in range(3):
            for j in range(3):
                lst.append(A[si+i][sj+j])
        if not chek(lst):
            print('No')
            exit()

print('Yes')
    
