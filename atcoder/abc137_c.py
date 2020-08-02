# https://atcoder.jp/contests/abc137/tasks/abc137_a

from collections import defaultdict
d = defaultdict(int)
N = int(input())
for i in range(N):
    s = input()
    ss = ''.join(sorted(s))
    d[ss] += 1
ans = 0
for k, v in d.items():
    ans += (v * (v-1)) //2
print(ans)


# N = int(input())
# d = dict()
# for i in range(N):
#     s = list(input())
#     s.sort()
#     s = ''.join(s)
#     if s in d:
#         d[s] += 1
#     else:
#         d[s] = 1

# ans = 0
# for i in d.values():
#     ans += (i * (i-1)) // 2

# print(ans)


# N = int(input())
# ss = []
# for i in range(N):
#     s = list(input())
#     s.sort()
#     ss.append(s)

# ss.sort()
# ans = 0
# tmp = 1
# for i in range(N-1):
#     if ss[i] == ss[i+1]:
#         tmp += 1
#         if i == N-2:
#             ans += (tmp * (tmp-1)) // 2
#     else:
#         ans += (tmp * (tmp-1)) // 2
#         tmp = 1

# print(ans)
