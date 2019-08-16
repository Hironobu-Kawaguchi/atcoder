# https://atcoder.jp/contests/abc032/tasks/abc032_b

s = input()
k = int(input())

st = set()
for i in range(len(s) - k + 1):
    st.add(s[i:i+k])
ans = len(st)
print(ans)
