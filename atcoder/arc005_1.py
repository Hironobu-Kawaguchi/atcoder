# https://atcoder.jp/contests/arc005/tasks/arc005_1

N = int(input())
w = input().split()
w[-1] = w[-1][:-1]
# print(w)
s = set(["TAKAHASHIKUN", "Takahashikun", "takahashikun"])

ans = 0
for x in w:
    if x in s:
        ans += 1
print(ans)
