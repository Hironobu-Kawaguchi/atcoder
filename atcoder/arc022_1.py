# https://atcoder.jp/contests/arc022/tasks/arc022_1

S = input()
S = S.upper()
# print(S)

ICT = "ICT"
i = 0
for s in S:
    if s == ICT[i]:
        i += 1
        if i == 3:
            break

if i == 3:
    print("YES")
else:
    print("NO")
