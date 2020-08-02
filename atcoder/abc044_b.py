# https://atcoder.jp/contests/abc044/tasks/abc044_b

w = input()
d = dict()

for i in range(len(w)):
    if w[i] in d:
        d[w[i]] += 1
    else:
        d[w[i]] = 1

ans = "Yes"
for k in d.keys():
    if d[k] % 2:
        ans = "No"
        break

print(ans)
