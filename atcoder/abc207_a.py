# https://atcoder.jp/contests/ABC207/tasks/abc207_a

abc = list(map(int, (input().split())))
ans = 0
for i in range(3):
    for j in range(3):
        if i==j: continue
        ans = max(ans, abc[i] + abc[j])
print(ans)

