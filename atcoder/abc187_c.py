# https://atcoder.jp/contests/abc187/tasks/abc187_c

n = int(input())
s = set()
for i in range(n):
    s.add(input())
ans = 'satisfiable'
for x in s:
    if ('!'+x) in s:
        ans = x
        break
print(ans)


# from collections import defaultdict

# n = int(input())
# d = defaultdict(int)
# for i in range(n):
#     s = input()
#     if s[0] == '!':
#         d[s[1:]] |= 1
#     else:
#         d[s] |= 2
# ans = 'satisfiable'
# for k,v in d.items():
#     if v==3:
#         ans = k
#         break
# print(ans)

