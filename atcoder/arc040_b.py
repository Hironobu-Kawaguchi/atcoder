# https://atcoder.jp/contests/arc040/tasks/arc040_b

n, r = map(int, input().split())
s = input()

# last = -1
# for i in range(n-1, -1, -1):
#     if s[i] == '.':
#         last = i
#         break
last = s.rfind('.')

ans = 0
i = 0
while i < n:
    if s[i] == '.':
        ans += 1
        i += r
    else:
        i += 1
ans += max(0, last-r+1)
print(ans)
