# https://atcoder.jp/contests/arc108/tasks/arc108_b

n = int(input())
s = input()
s = list(s)[::-1]
t = []

for i in range(n):
    t.append(s.pop())
    while len(t)>=3 and t[-3:]==['f','o','x']:
        for _ in range(3):
            t.pop()
print(len(t))


# n = int(input())
# s = input()
# num = 0
# lst = []
# i = 0
# while i<n:
#     if i<n-2:
#         if s[i:i+3] == 'fox':
#             num += 1
#             i += 3
#             continue
#     if i<n-1:
#         if s[i:i+2] == 'fo':
#             lst.append('fo')
#             i += 2
#             continue
#         if s[i:i+2] == 'ox':
#             if len(lst) and lst[-1]=='f':
#                 num += 1
#                 lst.pop()
#             else:
#                 lst = []
#             i += 2
#             continue
#     if s[i] == 'f':
#         lst.append('f')
#         i += 1
#         continue
#     elif s[i] == 'o':
#         if len(lst) and lst[-1]=='f':
#             lst[-1] = 'fo'
#             i += 1
#             continue
#         else:
#             lst = []
#             i += 1
#     elif s[i] == 'x':
#         if len(lst) and lst[-1]=='fo':
#             num += 1
#             lst.pop()
#             i += 1
#             continue
#         else:
#             lst = []
#             i += 1
#     else:
#         lst = []
#         i += 1

# print(n-num*3)



# TLE
# keyword = 'fox'
# n = int(input())
# s = input()
# ans = 0

# while True:
#     start = 0
#     cnt = 0
#     tmp = []
#     for i in range(n-2):
#         if s[i:i+3] == keyword:
#             ans += 1
#             cnt += 1
#             tmp.append(s[start:i])
#             start = i+3
#             n -= 3
#     if start<len(s):
#         tmp.append(s[start:])
#     s = ''.join(tmp)
#     if cnt==0:
#         break
# print(n)
# def main():
#     n = int(input())
#     for a in range(1,38):
#         for b in range(1,26):
#             if pow(3,a) + pow(5,b) == n:
#                 print(a, b)
#                 return
#     print(-1)
#     return

