# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_b

S = input()
w = int(input())
ans = ''
for i in range(len(S)):
    if i % w == 0:
        ans += S[i]
print(ans)
