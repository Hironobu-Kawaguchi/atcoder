# https://atcoder.jp/contests/abc073/tasks/abc073_c

N = int(input())
s = set()

for i in range(N):
    A = input()
    if A in s:
        s.remove(A)
    else:
        s.add(A)
print(len(s))
