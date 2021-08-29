# https://atcoder.jp/contests/abc216/tasks/abc216_d
# https://atcoder.jp/contests/abc216/submissions/25396173

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)
# M = next(it)

import sys
input = sys.stdin.buffer.readline
N, M = map(int, input().split())

top = [(-1, -1)] * (N + 1)
st = []
A = list()

def add_last(i):
    last = A[i][-1]
    if top[last]==(-1, -1):
        top[last] = (i, -1)
    else:
        top[last] = [top[last][0], i]
        st.append(last)

def pop_last(i):
    A[i].pop()
    if len(A[i]): add_last(i)

for i in range(M):
    l = []
    # k = next(it)
    # for j in range(k):
        # l.append(next(it))
    k = int(input())
    l = list(map(int, input().split()))
    l.reverse()
    A.append(l)
    add_last(i)

cnt = 0
while len(st):
    col = st[-1]
    st.pop()
    x, y = top[col]
    pop_last(x)
    pop_last(y)
    cnt += 1

if cnt==N:
    print("Yes")
else:
    print("No")



# # TLE
# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# N, M = map(int, input().split())
# stk = []
# top_set = set()
# top_idx = [-1] * (N+1)

# def pop_top(idx):
#     if len(stk[idx])==0: return
#     v = stk[idx][-1]
#     if v in top_set:
#         stk[idx].pop()
#         top_set.remove(stk[top_idx[v]].pop())
#         pop_top(idx)
#         pop_top(top_idx[v])
#     else:
#         top_set.add(v)
#         top_idx[v] = idx
#     return

# for i in range(M):
#     k = int(input())
#     a = list(map(int, (input().split())))
#     a = a[::-1]
#     stk.append(a)
#     pop_top(i)

# # print(stk)
# # print(top_set)
# # print(top_idx)

# if len(top_set):
#     ans = "No"
# else:
#     ans = "Yes"
# print(ans)

