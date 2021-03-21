# https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_a
# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

S = input()
ans = 'Yes'
if len(S)%2:
    ans = 'No'
else:
    for i, c in enumerate(S):
        if i%2 and c!='i':
            ans = 'No'
            break
        elif i%2 == 0 and c!='h':
            ans = 'No'
            break
print(ans)
