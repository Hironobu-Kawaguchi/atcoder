# https://atcoder.jp/contests/abc138/tasks/abc138_e

import string
s = input()
t = input()

d = dict(zip(string.ascii_lowercase, range(26)))    # アルファベットのdict
# print(d)
slist = [[] for _ in range(26)]
# tlist = [[] for _ in range(26)]
# print(slist)

for i in range(len(s)):
    k = d[s[i]]
    slist[k].append(i)
# for j in range(len(t)):
#     k = d[t[j]]
#     tlist[k].append(j)

# print(slist)
# print(tlist)

ans = 1     # 1文字目から
i, j = 0, 0
while j < len(t):
    k = d[t[j]]
    if len(slist[k]) == 0:    # 無ければ -1
        ans = -1
        j = len(t)
    else:
        for l in range(len(slist[k])):  # 1巡目
            if slist[k][l] > i:
                ans += slist[k][l] - i  # 増えた分を加算
                i = slist[k][l]
                break   # 見つかったら次のt
        else:   # 見つからなかったら
            ans += slist[k][0] + len(s) - i  # 1周して増えた分を加算
            i = slist[k][0] # 1周して見つからなければ、最初のを選択
        j += 1  # 次のt

print(ans)
