# https://atcoder.jp/contests/arc119/tasks/arc119_c

from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, (input().split())))
    cum = [0] * (N+1)
    for i in range(N):
        if i%2:
            cum[i+1] = cum[i] - A[i]
        else:
            cum[i+1] = cum[i] + A[i]
    d = defaultdict(int)
    for i in range(N+1):
        d[cum[i]] += 1
    # print(d)
    ans = 0
    for k, v in d.items():
        ans += v*(v-1)//2
    print(ans)
    return

main()


# TLE
# import copy

# def main():
#     N = int(input())
#     A = list(map(int, (input().split())))
#     ans = 0
#     ans_lst = []
#     for l in range(N-1):
#         for r in range(l+1, N):
#             lst = copy.deepcopy(A[l:r+1])
#             for i in range(len(lst)-1):
#                 dif = lst[i]
#                 lst[i] -= dif
#                 lst[i+1] -= dif
#             if lst[-1]==0:
#                 ans += 1
#                 ans_lst.append((l+1,r+1))
#                 # print(l+1, r+1, lst)
#     print(ans)
#     print(ans_lst)
#     return

# main()
