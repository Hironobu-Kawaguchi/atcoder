# https://atcoder.jp/contests/abc063/tasks/abc063_

S = input()
s = set()
for i in range(len(S)):
    s.add(S[i])
if len(s) == len(S):
    print("yes")
else:
    print("no")
