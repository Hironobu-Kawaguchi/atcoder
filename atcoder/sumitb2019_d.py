# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
# 最大 10**3

N = int(input())
S = input()
s1 = set()
s2 = set()
s3 = set()

for x in S:
    for y in s2:
        tmp = y+x
        if tmp not in s3:
            s3.add(tmp)
    for y in s1:
        tmp = y+x
        if tmp not in s2:
            s2.add(tmp)
    if x not in s1:
        s1.add(x)

print(len(s3))
