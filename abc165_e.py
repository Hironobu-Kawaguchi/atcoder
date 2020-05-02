# https://atcoder.jp/contests/abc165/tasks/abc165_e

def main():
    N, M = map(int, input().split())
    ans = []
    if N%2:
        for l in range(1, N//2+1):
            r = N-l
            ans.append([l,r])
    else:
        for l in range(1, N//2+1):
            r = N-l+1
            if l>N//4:
                r -= 1
            ans.append([l,r])
    for i in range(M):
        print(ans[i][0], ans[i][1])
    return
main()



# def main():
#     N, M = map(int, input().split())

#     def chk(x):
#         dist = set()
#         for a, b in x:
#             d1 = abs(b-a)
#             d2 = N-d1
#             if d1 == d2:
#                 return False
#             if d1 in dist or d2 in dist:
#                 return False
#             dist.add(d1)
#             dist.add(d2)
#         return True

#     ans = []
#     done = set()
#     dist = set()
#     d = 1
#     for i in range(N//2-1,-1,-1):
#         while True:
#             if i not in done and (i+d) not in done:
#                 ans.append([i,i+d])
#                 done.add(i)
#                 done.add(i+d)
#                 dist.add(d)
#                 dist.add(N-d)
#                 break
#             d += 1
#             if d >= N:
#                 d = 1
#         if len(ans) == M:
#             break
#     if chk(ans):
#         for a, b in ans:
#             print(a+1, b+1)
#         return
#     else:
#         print("dame")
#         return
# main()


# from itertools import permutations

# def main():
#     N, M = map(int, input().split())

#     def chk(x):
#         dist = set()
#         for a, b in x:
#             d1 = abs(b-a)
#             d2 = N-d1
#             if d1 == d2:
#                 return False
#             if d1 in dist or d2 in dist:
#                 return False
#             dist.add(d1)
#             dist.add(d2)
#         return True

#     for comb in permutations(range(N), M*2):
#         # print(comb)
#         ans = []
#         for i in range(M):
#             ans.append([comb[2*i], comb[2*i+1]])
#         if chk(ans):
#             print(ans)
#             return
# main()
