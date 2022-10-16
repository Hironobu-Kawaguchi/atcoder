# https://atcoder.jp/contests/arc142/tasks/arc142_a

def main():
    N, K = map(int, input().split())
    S = input()
    zeros = 0
    for j in range(K):
        if S[j]=='0':
            zeros += 1
    ones = 0
    for j in range(K,N):
        if S[j]=='1':
            ones += 1
    cnt = 0
    for i in range(N-K+1):
        if zeros==0 and ones==0: cnt += 1
        if S[i]=='0': zeros -= 1
        elif S[i]=='1': ones += 1
        if i+K<N and S[i+K]=='0': zeros += 1
        elif i+K<N and S[i+K]=='1': ones -= 1
    # print(cnt)
    if cnt==1:
        print('Yes')
    else:
        print('No')
    return

T = int(input())
for ti in range(T):
    main()


# def main():
#     N, K = map(int, input().split())
#     S = input()
#     ans = 'No'
#     l1, r1 = -1, -1
#     for i in range(N):
#         if S[i]=='1':
#             if l1==-1: l1 = i
#             r1 = i
#     # print(l1, r1)
#     if l1==-1:
#         numk = 0
#         cnt = 0
#         for i in range(N):
#             if S[i]=='?': cnt += 1
#             else:
#                 if cnt==K: numk += 1
#                 cnt = 0
#             if cnt>K:
#                 print(ans)
#                 return
#         else:
#             if cnt==K: numk += 1
#         if numk==1: ans = 'Yes'
#         print(ans)
#         return
#     if r1-l1+1>K:
#         print(ans)
#         return
#     for i in range(l1, r1+1):
#         if S[i]=='0':
#             print(ans)
#             return
#     lr0 = -1
#     for i in range(l1):
#         if S[i]=='0':
#             lr0 = i
#     rl0 = N
#     for i in range(r1+1,N):
#         if S[i]=='0':
#             rl0 = i
#             break
#     # print(l1, r1, lr0, rl0)
#     l = lr0+1
#     if r1!=-1: l = max(l, r1-K+1)
#     if l1!=-1: l = min(l, l1)
#     r = rl0-1
#     if l1!=-1: r = min(r, l1+K-1)
#     if r1!=-1: r = max(r, r1)
#     # print(K, l, r)
#     if r-l+1==K:
#         ans = 'Yes'
#     print(ans)
#     return

# T = int(input())
# for t in range(T):
#     main()

