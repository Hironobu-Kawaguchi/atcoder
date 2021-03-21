# https://atcoder.jp/contests/abc017/tasks/abc017_2

X = input()
ans = "YES"
i = 0
while i < len(X):
    if X[i] in ['o', 'k', 'u']:
        i += 1
    elif X[i:i+2] == "ch":
        i += 2
    else:
        ans = "NO"
        break
print(ans)
