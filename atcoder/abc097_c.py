# https://atcoder.jp/contests/abc097/tasks/abc097_c

s = input()
K = int(input())
N = len(s)

st = set()
for i in range(N):
    for j in range(i+1, min(i+K+1, N+1)):
        st.add(s[i:j])
l = sorted(list(st))

ans = l[K-1]
print(ans)
