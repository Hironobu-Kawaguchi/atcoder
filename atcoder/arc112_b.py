# https://atcoder.jp/contests/arc112/tasks/arc112_b

B, C = map(int, input().split())
ans = 0
ans += max(C-2,0)//2 + (C//2) + 1
if C>=1:
    ans += max(C-1,0)//2 + max(C-1,0)//2 + 1
if B>=0 and (max((C-1),0)//2-B)>=0:
    ans -= (max(C-1,0)//2-B) - (B-C//2) + 1
elif B<0 and (max((C-2),0)//2+B)>=0:
    ans -= (max(C-2,0)//2+B) - (-B-(max(C-1,0)//2)) + 1
ans = max(ans, max(C-2,0)//2 + (C//2) + 1)  # そのままで最大
if B==0:
    ans = max(ans, max(C-1,0)//2 + (C//2) + 1)  # そのままで最大
print(ans)


# import sys
# # input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# cnt = 0

# def dfs(b, c, st):
#     global cnt
#     cnt = max(cnt, len(st))
#     if c==0: return
#     if c>=2:
#         st.add(b-1)
#         dfs(b-1, c-2, st)
#     if c>=1:
#         st.add(-b)
#         dfs(-b, c-1, st)
#     return

# for B in range(-10, 11):
#     for C in range(0, 11):
#         ans = 0
#         ans += max(C-2,0)//2 + (C//2) + 1
#         if C>=1:
#             ans += max(C-1,0)//2 + max(C-1,0)//2 + 1
#         if B>=0 and (max((C-1),0)//2-B)>=0:
#             ans -= (max(C-1,0)//2-B) - (B-C//2) + 1
#         elif B<0 and (max((C-2),0)//2+B)>=0:
#             ans -= (max(C-2,0)//2+B) - (-B-(max(C-1,0)//2)) + 1
#         ans = max(ans, max(C-2,0)//2 + (C//2) + 1)  # そのままで最大
#         if B==0:
#             ans = max(ans, max(C-1,0)//2 + (C//2) + 1)  # そのままで最大
#         cnt = 0
#         dfs(B, C, set([B]))
#         # print(B, C, cnt, ans)
#         if ans!=cnt:
#             print(B, C, cnt, ans)
# print('finish')
