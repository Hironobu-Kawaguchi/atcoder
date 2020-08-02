# B - *e**** ********e* *e****e* ****e**
# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_b

N = int(input())
S = input()
K = int(input())

sk = S[K-1]
out = ''

for s in S:
    if s != sk:
        out += '*'
    else:
        out += sk
print(out)
    